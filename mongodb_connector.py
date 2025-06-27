from pymongo import MongoClient
from datetime import datetime

def connect_to_mongo():
    """Устанавливает и возвращает соединение с коллекцией MongoDB."""
    client = MongoClient(
        "mongodb://ich_editor:verystrongpassword"
        "@mongo.itcareerhub.de/?readPreference=primary"
        "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
    )
    db = client["ich_edit"]
    collection = db["final_project_100125_stakun_elena"]
    return client, collection

def log_search_to_mongo(search_type: str, params: dict, results_count: int):
    """Записывает структуру запроса в коллекцию MongoDB."""
    client, collection = connect_to_mongo()

    log_entry = {
        "timestamp": datetime.now().isoformat(timespec='seconds'),
        "search_type": search_type,
        "params": params,
        "results_count": results_count
    }

    result = collection.insert_one(log_entry)
    print(f"Log inserted with ID: {result.inserted_id}")

    client.close()
    
def clear_log_collection():
    """Очищает коллекцию final_project_100125_stakun_elena."""
    client, collection = connect_to_mongo()
    result = collection.delete_many({})
    print(f"{result.deleted_count} documents deleted from the collection.")
    client.close()
