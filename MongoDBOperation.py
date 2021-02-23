# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 06:06:50 2021

@author: AvnishYadav
"""
# importing mongodb file
import pymongo
import json
import pandas as pd


class MongoDBOperation:
    def __init__(self):
        self.user_name = "Avnish"
        self.password = "Aa327030"
        self.DB_URL = 'mongodb+srv://{0}:{1}@cluster0.5fvxl.mongodb.net/<dbname>?retryWrites=true&w=majority'.format(
            self.user_name, self.password)

    def getDatabaseClientObject(self):
        """
        Return pymongoClient object to perform action with MongoDB
        """
        try:
            self.client = pymongo.MongoClient(self.DB_URL)  # creating database client object
            return self.client
        except Exception as e:
            raise Exception(
                "Error occured in class: MongoDBOperation method:getDataBaseClientObject error:Failed to create database connection object-->" + str(
                    e))

    def closeDatabaseClientobject(self, obj_name):
        """
        

        Parameters
        ----------
        obj_name : pymongo client
            DESCRIPTION.pymongo client object 

        Raises
        ------
        Exception
            Failed to close database connection-->.

        Returns
        -------
        bool
            True if connection closed.

        """
        try:
            obj_name.close()
            return True
        except Exception as e:
            raise Exception(
                "Error occured in class: MongoDBOperation method:closeDatabaseClientobject error:Failed to close database connection-->" + str(
                    e))

    def checkDataBase(self, client, db_name):
        """

        Parameters
        ----------
        client : pymongo client
            DESCRIPTION. object which will be used to fetch communicate with mongo db
        db_name : string
            database name.

        Raises
        ------
        Exception
            DESCRIPTION.If any exception occurs

        Returns
        -------
        bool
            True if database already exists.

        """
        try:
            if db_name in client.list_database_names():
                return True
            else:
                return False
        except Exception as e:
            raise Exception(
                "Error occured in class: MongoDBOperation method:checkDataBase error:Failed to check database exist or not" + str(
                    e))

    def createDatabase(self, client, db_name):
        """
        client: client object of database
        db_name:data base name
        """
        try:
            return client[db_name]
        except Exception as e:
            raise Exception("Error occured in class: MongoDBOperation method: createDatabase error:" + str(e))

    def createCollectionInDatabase(self, database, collection_name):
        """
        database:database
        collection_name: name of collection
        return:
            collection object
        """
        try:
            return database[collection_name]
        except Exception as e:
            raise Exception(
                "Error occured in class: MongoDBOperation method:createCollectionInDatabase  error: " + str(e))

    def checkExistenceCollection(self, collection_name, database):
        """
        

        Parameters
        ----------
        collection_name : collection_name
            DESCRIPTION.collection name which needs to verify
        database : TYPE
            DESCRIPTION.database in which collection needs to check for existence

        Raises
        ------
        Exception
            DESCRIPTION.

        Returns
        -------
        bool
            true if collection present in database.

        """
        try:
            """It verifies the existence of collection name in a database"""
            collection_list = database.list_collection_names()

            if collection_name in collection_list:
                # print("Collection:'{COLLECTION_NAME}' in Database:'{DB_NAME}' exists")
                return True

            # print(f"Collection:'{COLLECTION_NAME}' in Database:'{DB_NAME}' does not exists OR \n        no documents are present in the collection")
            return False
        except Exception as e:
            raise Exception("Error occured in class: MongoDBOperation method:checkExistenceCollection error:" + str(e))

    def getCollection(self, collection_name, database):
        """
        collection_name:collection name
        database=database
        ------------------------------------------
        return collection object
        """
        try:
            collection = self.createCollectionInDatabase(database, collection_name)
            return collection
        except Exception as e:
            raise Exception(
                "Error occured in class: MongoDBOperation method:getCollection error:Failed to find collection" + str(
                    e))

    def isRecordPresent(self, db_name, collection_name, record):
        """
        db_name: database name
        collection_name: collection name 
        record: records to search 
        ----------------------------------------------
        return True if record exists else return false
        """
        try:
            client = self.getDatabaseClientObject()
            database = self.createDatabase(client, db_name)
            collection = self.getCollection(collection_name, database)
            recordfound = collection.find(record)
            if recordfound.count() > 0:
                client.close()
                return True
            else:
                client.close()
                return False
        except Exception as e:
            client.close()
            raise Exception(
                "Error occured in class: MongoDBOperation method:isRecordPresent error:Failed to insert record " + str(
                    e))

    def createOneRecord(self, collection, data):
        """
        collection: Accept collection name
        data: accept single to insert into collection
        -------------------------------------------
        return 1 if record inserted
        """
        try:
            collection.insert_one(data)  # insertion of record in collection
            print("Record inserted")
            return 1
        except Exception as e:
            raise Exception(
                "Error occured in class: MongoDBOperation method:createOneRecord error:Failed to insert record " + str(
                    e))

    def createMutlipleRows(self, collection, data):
        """
        collection: collection object
        data: data which needs to be inserted 
        --------------------------------------------
        return no of record inserted
        """
        try:
            collection.insert_many(data)
            return len(data)
        except Exception as e:
            raise Exception(
                "Error occured in class: MongoDBOperation method:createMultipleRows error:Failed to insert record " + str(
                    e))

    def insertRecordInCollection(self, db_name, collection_name, record):
        """
        db_name: database name
        collection_name: collection name 
        record: records to insert
        ------------------------------
        return No of record inserted(int).
        """
        try:
            no_of_row_inserted = 0
            client = self.getDatabaseClientObject()
            database = self.createDatabase(client, db_name)
            collection = self.getCollection(collection_name, database)
            if not self.isRecordPresent(db_name, collection_name, record):
                no_of_row_inserted = self.createOneRecord(collection=collection, data=record)
            client.close()
            return no_of_row_inserted
        except Exception as e:
            raise Exception(
                "Error occured in class: MongoDBOperation method:insertRecordInCollection error:Failed to insert record " + str(
                    e))


    def dropCollection(self,db_name,collection_name):
        """

        :param db_name: database name
        :param collection_name:  collection name
        :return: True if collection droped successfully.
        """
        try:
            client=self.getDatabaseClientObject()
            database=self.createDatabase(client,db_name)
            if self.checkExistenceCollection(collection_name,database):
                collection_name=self.getCollection(collection_name,database)
                collection_name.drop()
            return True
        except Exception as e:
            raise Exception("Error occured in class MongoDBOperation method drop collection error:"+str(e))


    def insertRecordsInCollection(self, db_name, collection_name, records):
        """
        db_name: database name
        collection_name: collection name 
        records: records to insert 
        """
        try:
            no_of_row_inserted = 0
            client = self.getDatabaseClientObject()
            database = self.createDatabase(client, db_name)
            collection = self.getCollection(collection_name, database)
            for record in records:
                if not self.isRecordPresent(db_name, collection_name, record):
                    no_of_row_inserted = no_of_row_inserted + self.createOneRecord(collection=collection, data=records)
            client.close()
            return no_of_row_inserted
        except Exception as e:
            client.close()
            raise Exception(
                "Error occured in class: MongoDBOperation method:insertRecordsInCollection error:Failed to insert record " + str(
                    e))

    def insertDataFrame(self, db_name, collection_name, data_frame):
        """
        db_name:Database Name
        collection_name: collection name
        data_frame: dataframe which needs to be inserted
        return:
            
        """
        try:
            no_of_row_inserted = 0
            records = list(json.loads(data_frame.T.to_json()).values())
            client = self.getDatabaseClientObject()
            database = self.createDatabase(client, db_name)
            collection = self.getCollection(collection_name, database)
            collection.insert_many(records)
            """
            for record in records:
                if not self.isRecordPresent(db_name, collection_name, record):
                    no_of_row_inserted = no_of_row_inserted + self.insertRecordInCollection(db_name, collection_name,
                                                                                          record)
            """
            return len(records)
        except Exception as e:
            raise Exception(
                "Error occured in class: MongoDBOperation method:insertDataFrame error: Not able to insert dataframe into collection " + str(
                    e))

    def getDataFrameofCollection(self, db_name, collection_name):
        """
        

        Parameters
        ----------
        db_name : string
            DESCRIPTION. database name
        collection_name : string
            DESCRIPTION.collection name

        Returns
        -------
        Pandas data frame of  collection name present database.

        """
        try:
            client = self.getDatabaseClientObject()
            database = self.createDatabase(client, db_name)
            collection = self.getCollection(collection_name=collection_name, database=database)
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"],axis=1)
            return df
        except Exception as e:
            raise Exception("Error in Class: MongoDBOperation method:getDataFrameofCollection error:   " + str(e))
