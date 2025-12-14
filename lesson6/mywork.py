import csv
import json
users = {}
with open('purchase_log.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                data = json.loads(line)
                user_id = data.get('user_id')
                category = data.get('category')
                if user_id != 'user_id' and user_id and category:
                    users[user_id] = category
            except:
                pass
with open ('visit_log__1_.csv', 'r') as doc_in, open('funnel.csv', 'w') as doc_out:
    title = doc_in.readline().strip()
    doc_out.write(title + ',category' '\n')
    for line in doc_in:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            user_id = parts[0]
            source = parts[1]
            if user_id in users:
                category = users[user_id]
                doc_out.write(f'{user_id},{source},{category}\n')
