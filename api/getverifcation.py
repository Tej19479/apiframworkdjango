from account.databaseconnection import dbconnection


class verification:
    def kyccheck(givendata):
            required_data = [('Kyc_Document',), ('Account_details',), ('PAN',)]
            b = []
            for data in required_data:
              a = True
              for x in givendata:
                  if x[0].upper() == data[0].upper():
                    a = False
                    break
              if a:
                  b.append(data[0])

            return b

    def getverication(inv_id):

        try:
            query = f"SELECT id ,inv_state,uid_id FROM api_inv where  id ={inv_id}"
            cursor = dbconnection["sql"].cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            if len(results)>0:
                if results[0][0] or results[0][1]:
                    kyc_count = f"SELECT distinct(verification_type) FROM api_user_verification where  uid ={results[0][2]}"
                    cursor.execute(kyc_count)
                    results = cursor.fetchall()
                    rs= verification.kyccheck(results)
                    data={"status":True,"pending_document":rs}
                    return data
            else:
                data={"status":False,"Investment":"investemnt id not resgister"}
                return data
        except Exception as e:
            print(Exception)

        
