from flask_app.config.mysqlconnection import connectToMySQL
# imports mysqlconnection file for DB queries
from flask_app import app
from flask_app import DATABASE
#imports global variable name for DB schema
from flask import flash
from flask_app.models import item_model

class category:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_by_id(cls,data):
        query = """
            SELECT * FROM categories LEFT JOIN items ON categories.id = items.category_id
            WHERE categories.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            category_instance = cls(results[0])
            items_list = []
            for row_in_db in results:
                item_data = {
                    'id' : row_in_db['items.id'],
                    'category_id' : row_in_db['category_id'],
                    'name' : row_in_db['items.name'],
                    'num' : row_in_db['num'],
                    'description' : row_in_db['description'],
                    'price' : row_in_db['price'],
                    'imageurl' : row_in_db['imageurl'],
                    'created_at' : row_in_db['created_at'],
                    'updated_at' : row_in_db['updated_at']
                }
                item_instance = item_model.item(item_data)
                items_list.append(item_instance)
                
            category_instance.items = items_list
            return category_instance
        else:
            return False
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM categories;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_categories = []
        for one_row in results:
            this_category_instance = cls(one_row)
            all_categories.append(this_category_instance)
        return all_categories
    
    