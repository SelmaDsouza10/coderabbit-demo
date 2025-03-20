def process_data(data):
    results = []
    for item in data:
        if item['status'] == 'active':
            if 'last_login' in item:
                if item['last_login'] > '2023-01-01':
                    if item['value'] > 100:
                        results.append({
                            'id': item['id'],
                            'value': item['value'] * 1.1
                        })
    return results