from datetime import datetime
from flask import Blueprint, current_app, jsonify, render_template, request

bp = Blueprint('main', __name__)
CATEGORIES = {'Pessoal', 'Trabalho', 'Estudos', 'Saúde', 'Medicamentos'}
REPEATS = {'none', 'daily', 'weekly'}

def db():
    return current_app.get_db()

def serialize(row):
    return dict(row)

def validate(payload):
    title = str(payload.get('title', '')).strip()
    description = str(payload.get('description', '')).strip()
    category = str(payload.get('category', 'Pessoal'))
    due_at = str(payload.get('due_at', '')).strip()
    repeat_rule = str(payload.get('repeat_rule', 'none'))
    if not 1 <= len(title) <= 100:
        return None, 'O título deve ter entre 1 e 100 caracteres.'
    if len(description) > 500:
        return None, 'A descrição deve ter até 500 caracteres.'
    if category not in CATEGORIES or repeat_rule not in REPEATS:
        return None, 'Categoria ou repetição inválida.'
    try:
        datetime.strptime(due_at, '%Y-%m-%dT%H:%M')
    except ValueError:
        return None, 'Informe uma data e horário válidos.'
    return (title, description, category, due_at, repeat_rule), None

@bp.get('/')
def home():
    return render_template('index.html')

@bp.get('/api/reminders')
def list_reminders():
    rows = db().execute('SELECT * FROM reminders ORDER BY completed ASC, due_at ASC, id DESC').fetchall()
    return jsonify([serialize(r) for r in rows])

@bp.post('/api/reminders')
def create_reminder():
    values, error = validate(request.get_json(silent=True) or {})
    if error:
        return jsonify(error=error), 400
    cursor = db().execute('INSERT INTO reminders (title,description,category,due_at,repeat_rule) VALUES (?,?,?,?,?)', values)
    db().commit()
    return jsonify(serialize(db().execute('SELECT * FROM reminders WHERE id=?', (cursor.lastrowid,)).fetchone())), 201

@bp.put('/api/reminders/<int:item_id>')
def update_reminder(item_id):
    if not db().execute('SELECT id FROM reminders WHERE id=?', (item_id,)).fetchone():
        return jsonify(error='Lembrete não encontrado.'), 404
    values, error = validate(request.get_json(silent=True) or {})
    if error:
        return jsonify(error=error), 400
    db().execute('UPDATE reminders SET title=?,description=?,category=?,due_at=?,repeat_rule=? WHERE id=?', (*values, item_id))
    db().commit()
    return jsonify(serialize(db().execute('SELECT * FROM reminders WHERE id=?', (item_id,)).fetchone()))

@bp.patch('/api/reminders/<int:item_id>/complete')
def complete_reminder(item_id):
    payload = request.get_json(silent=True) or {}
    if type(payload.get('completed')) is not bool:
        return jsonify(error='Informe completed como verdadeiro ou falso.'), 400
    cursor = db().execute('UPDATE reminders SET completed=? WHERE id=?', (int(payload['completed']), item_id))
    db().commit()
    if cursor.rowcount == 0:
        return jsonify(error='Lembrete não encontrado.'), 404
    return jsonify(serialize(db().execute('SELECT * FROM reminders WHERE id=?', (item_id,)).fetchone()))

@bp.delete('/api/reminders/<int:item_id>')
def delete_reminder(item_id):
    cursor = db().execute('DELETE FROM reminders WHERE id=?', (item_id,))
    db().commit()
    if cursor.rowcount == 0:
        return jsonify(error='Lembrete não encontrado.'), 404
    return '', 204
