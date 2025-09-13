import json
import os
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('TABLE_NAME', 'StudentRecords'))

def _response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps(body)
    }

def _validate_student(student, require_all=True):
    required = ["student_id", "name", "course"]
    if require_all:
        missing = [k for k in required if k not in student or student[k] in (None, "")]
        if missing:
            return False, f"Missing required fields: {', '.join(missing)}"
    else:
        if "student_id" not in student or not student["student_id"]:
            return False, "Missing required field: student_id"
    return True, None

def create_student(event):
    try:
        student = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return _response(400, {"error": "Invalid JSON"})
    ok, err = _validate_student(student, require_all=True)
    if not ok:
        return _response(400, {"error": err})
    table.put_item(Item=student, ConditionExpression="attribute_not_exists(student_id)")
    return _response(201, {"message": "Student record added", "student_id": student["student_id"]})

def get_student(event):
    params = event.get("queryStringParameters") or {}
    student_id = params.get("student_id")
    if not student_id:
        return _response(400, {"error": "Query parameter 'student_id' is required"})
    res = table.get_item(Key={"student_id": student_id})
    item = res.get("Item")
    if not item:
        return _response(404, {"error": "Student not found"})
    return _response(200, item)

def update_student(event):
    try:
        payload = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return _response(400, {"error": "Invalid JSON"})
    ok, err = _validate_student(payload, require_all=False)
    if not ok:
        return _response(400, {"error": err})

    student_id = payload["student_id"]
    update_fields = {k: v for k, v in payload.items() if k != "student_id"}
    if not update_fields:
        return _response(400, {"error": "No fields to update"})

    expr_names = {}
    expr_values = {}
    set_clauses = []
    for i, (k, v) in enumerate(update_fields.items(), start=1):
        name_key = f"#f{i}"
        value_key = f":v{i}"
        expr_names[name_key] = k
        expr_values[value_key] = Decimal(str(v)) if isinstance(v, (int, float)) else v
        set_clauses.append(f"{name_key} = {value_key}")

    update_expr = "SET " + ", ".join(set_clauses)

    res = table.update_item(
        Key={"student_id": student_id},
        UpdateExpression=update_expr,
        ExpressionAttributeNames=expr_names,
        ExpressionAttributeValues=expr_values,
        ConditionExpression="attribute_exists(student_id)",
        ReturnValues="ALL_NEW"
    )
    return _response(200, {"message": "Student updated", "item": res["Attributes"]})

def delete_student(event):
    params = event.get("queryStringParameters") or {}
    student_id = params.get("student_id")
    if not student_id:
        return _response(400, {"error": "Query parameter 'student_id' is required"})
    table.delete_item(
        Key={"student_id": student_id},
        ConditionExpression="attribute_exists(student_id)"
    )
    return _response(200, {"message": "Student deleted", "student_id": student_id})

def lambda_handler(event, context):
    method = (event.get("httpMethod") or "").upper()

    try:
        if method == "OPTIONS":
            return _response(200, {"ok": True})
        elif method == "POST":
            return create_student(event)
        elif method == "GET":
            return get_student(event)
        elif method == "PUT":
            return update_student(event)
        elif method == "DELETE":
            return delete_student(event)
        else:
            return _response(405, {"error": f"Method {method} not allowed"})
    except Exception as e:
        return _response(500, {"error": str(e)})

