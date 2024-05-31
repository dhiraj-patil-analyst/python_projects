'''
employee -object

details need to fetch

'''

import flask

app=flask(__name__)
employees=[]
@app.route('/add employee',methods=['Post'])

def add_employee():
    if 'name' in data:
        employee_name=data['name']
        employees.append(employee_name)
        return jsonify({message:'Employee name added successfully','Employee_name':employee_name}),201
    else:
        return jsonify({'Error':'name is required in request data'}),400
        if__name__=='__main__':
    app.run(debug=True)
            
    
        
        
        
        