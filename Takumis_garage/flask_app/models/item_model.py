from flask_app.config.mysqlconnection import connectToMySQL
# imports mysqlconnection file for DB queries
from flask_app import app
from flask_app import DATABASE
#imports global variable name for DB schema
from flask import flash
# import flash for validation

# example of init class
class item:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.num = data['num']
        self.description = data['description']
        self.price = data['price']
        self.imageurl = data['imageurl']
        self.category_id = data['category_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# get item by its ID
    @classmethod
    def get_by_id(cls,data):
        query = """
            SELECT * FROM items WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False