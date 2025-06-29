 with open("teacher.json", "w" ,encoding= "UTF-8") as file:
            content = json.dumps(teachers, indent=2)
            file.write(content)