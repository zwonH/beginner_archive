from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

order_list = []
order_no = 1

@app.route('/')
def home():
    return 'Let\'s get some orders for Ollie!'

@app.route('/photocard')
def photocard():
   return render_template('olinka.html')

@app.route('/orderlist')
def orderlist():
   return render_template('orderlist.html')

@app.route('/order', methods=['POST'])
def order():
    global order_list
    global order_no

    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    mobile_receive = request.form['mobile_give']

    order = {'no': order_no, 'name': name_receive, 'quantity': quantity_receive, 'address': address_receive, 'mobile': mobile_receive}

    order_no += 1
    order_list.append(order)

    return jsonify({'result': 'success'})


@app.route('/order', methods=['GET'])
def view():
    return jsonify({'result': 'success', 'order_list':order_list})


@app.route('/delete', methods=['POST'])
def delete():
    global order_list
    no_receive = request.form['no_give']

    for order in order_list:
        if str(order['no']) == no_receive:
            order_list.remove(order)
            return jsonify({'result': 'success'})

    return jsonify ({'result': 'fail', 'msg': '해당 주문이 없습니다'})

if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)