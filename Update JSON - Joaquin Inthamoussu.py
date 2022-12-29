import requests
import time

response1 = requests.get("https://web/v1")
response2 = requests.get("https://web/v2")
response3 = requests.get("https://web/v3")

correct_response1 = False
correct_response2 = False
correct_response3 = False

return_final_json = []

# respone1: Loop hasta recibir respuesta 200
while correct_response1 != True:
    if response1.status_code != 200:
        print("No se puede obtener respuesta: v1!")
        time.sleep(5)
    else:
        count = 0
        
        while count < len(response1.json()):
            return_final_json.append(response1.json()[count])
            count+=1
    
        print("---------- v1 -----------")
        print(return_final_json)
        print("-------------------------\n")
        
        
        
        # respone2: Loop hasta recibir respuesta 200
        while correct_response2 != True:
            if response2.status_code != 200:
                print("No se puede obtener respuesta: v2!")
                time.sleep(5)
            else:
                count = 0
                
                while count < len(response2.json()):
                    count2 = 0
                    
                    while count2 < len(return_final_json):
                        # Comparar que sea el mismo {'name': '##'} del response2 y return_final_json
                        if response2.json()[count]['name'] == return_final_json[count2]['name']:
                            json_aux = {}
                            
                            # Buscar los key values del response2
                            for key in response2.json()[count]:
                                
                                # json_aux para ordenar los campos
                                json_aux[key] = ""
                                
                                if key == 'category':
                                    # Cuando encuentra el {'category': '##'} de response2 se lo asigna a return_final_json y después se elimina la key 'tag'
                                    return_final_json[count2][key] = response2.json()[count][key]
                                    del return_final_json[count2]['tag']
                                    
                            # Ordenar los campos
                            for key in return_final_json[count2]:
                                # Accedo a cada key y le asigno el contenido de return_final_json a json_aux (Ordenado)
                                json_aux[key] = return_final_json[count2][key]
                            
                            # Asigno el contenido de json_aux a return_final_json (Para tenerlo todo ordenado en el return_json_final)
                            return_final_json[count2] = json_aux
                            
                        count2+=1
                    
                    count+=1
                
                print("---------- v2 -----------")
                print(return_final_json)
                print("-------------------------\n")
                
                
                
                # respone3: Loop hasta recibir respuesta 200
                while correct_response3 != True:
                    if response3.status_code != 200:
                        print("No se puede obtener respuesta: v3!")
                        time.sleep(5)
                    else:
                        count = 0
                        
                        while count < len(response3.json()):
                            count2 = 0
                        
                            while count2 < len(return_final_json):
                                # Comparar que sea el mismo {'name': '##'} del response3 y return_final_json
                                if response3.json()[count]['name'] == return_final_json[count2]['name']:
                                    json_aux = {}
                                    
                                    # Buscar los key values del json_v3
                                    for key in response3.json()[count]:
                                        
                                        if key == 'family':
                                            # Almacenar: {'family': '##'} del response3 y eliminar 'category'
                                            json_aux[key] = response3.json()[count][key]
                                            del return_final_json[count2]['category']
                                            
                                        if key == 'mass':
                                            # Cuando encuentra el {'mass': '##'} de response3 se lo asigna a return_final_json y después se elimina la key 'weight'
                                            return_final_json[count2][key] = response3.json()[count][key]
                                            del return_final_json[count2]['weight']
                                        
                                        if key == 'mass_unit':
                                            # Cuando encuentra el {'mass_unit': '##'} de response3 se lo asigna a return_final_json y después se elimina la key 'weight_unit'
                                            return_final_json[count2][key] = response3.json()[count][key]
                                            del return_final_json[count2]['weight_unit']
                                    
                                    # Añado el campo family a return_final_json
                                    return_final_json[count2]['family'] = json_aux['family']
                                    # Añado el campo user a return_final_json
                                    return_final_json[count2]['user'] = 'anonymous'
                                    
                                count2+=1
                        
                            count+=1 
                        
                        print("---------- v3 -----------")
                        print(return_final_json)
                        print("-------------------------\n")
                        
                        correct_response3 = True
                
                correct_response2 = True
        
        correct_response1 = True
