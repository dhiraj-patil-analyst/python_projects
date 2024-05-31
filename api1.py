'''
Fetch the details of the from data

'''

from flask import Flask,jsonify
app=flask(__name__)

employees=['Genpact','MRO','Capegemini','TCS']

@app.route('/Get employee ',methods=['GET'])


def get_employee(index):
    if index <len(employees):
        return jsonify({'employee_name':employees[index]})
    else:
        return jsonify({'error':'Employee not found'}),404
    if __name__ =='__main__':
        app.run(debug=True)
    
