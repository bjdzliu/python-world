from flask import Flask,request,Response
from flask import render_template
import vpcops,getuniqid
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/formtest',methods=["POST"])
def formtest():
    if request.method == 'POST':
        a = request.get_json()
        contentType=request.headers['Content-Type']
        print a,contentType
        return "aaaa"
        b=json.loads(a)
        modified_dict=dict(title=b['title'], age=20, score=88)
        # b=json.dumps(a)
        # print b,type(b),a,type(a)
        # d = dict(name='Bob', age=20, score=88)
        output=json.dumps(modified_dict)
        return output
    else:
        return '<h1>post</h1>'


@app.route('/query',methods=["POST","GET"])
def query():
    # content = json.dumps({"error_code": "1001"})
    # return content
    if request.method == 'GET':
        mydict = {}
        return render_template('createAccept.html',mydict=mydict)
    else:
        userid = request.form['userid']
        akid = request.form['akid']
        secret = request.form['secret']
        region = request.form['region']
        query_region = request.form['query_region']
        resultdict = vpcops.query(akid,secret,region,query_region)
    if resultdict.has_key('error'):
        return render_template('createAccept.html',mydict=resultdict)
    else:
        #vrouterid=resultdict['RouterInterfaceSet']['RouterInterfaceType'][0]['RouterId']
        vrouterid=getuniqid.getuniqid(resultdict)
        mydict = dict(userid=userid, akid=akid,secret=secret,region=region,query_region=query_region)
                #create a dict
                #print vrouterid
                #return dict
        return render_template('createAccept.html',mydict=mydict,vrouterid=vrouterid)

@app.route('/createaccept', methods=["POST"])
def createaccept():
            if request.method == 'POST':
                print request.get_json()
                a = request.get_data()
                contentType = request.headers['Content-Type']
                print  "contentTyp is :"+ contentType
                b = json.loads(a)
                RouterInterfaceId = vpcops.createaccept(b)
                print RouterInterfaceId
                result={'RouterInterfaceId':RouterInterfaceId,'result_message':'success'}
                output = json.dumps(result)
                return output
            else:
                return '<h1>post</h1>'

@app.route('/query2', methods=["POST","GET"])
def query2():
    # content = json.dumps({"error_code": "1001"})
    # return content
    if request.method == 'GET':
        mydict = {}
        return render_template('createInit.html',mydict=mydict)
    elif request.method == 'POST':
        userid = request.form['userid']
        akid = request.form['akid']
        secret = request.form['secret']
        region = request.form['region']
        query_region = request.form['query_region']
        resultdict = vpcops.query(akid,secret,region,query_region)
    else:
        pass
    if resultdict.has_key('error'):
        return render_template('createInit.html',mydict=resultdict)
    else:
        #vrouterid=resultdict['RouterInterfaceSet']['RouterInterfaceType'][0]['RouterId']
        vrouterid=getuniqid.getuniqid(resultdict)
        mydict = dict(userid=userid, akid=akid,secret=secret,region=region,query_region=query_region)
                #create a dict
                #print vrouterid
                #return dict
        return render_template('createInit.html',mydict=mydict,vrouterid=vrouterid)

@app.route('/createinit', methods=["POST"])
def createinit():
    if request.method == 'POST':
        a = request.get_data()
        b = json.loads(a)
        RouterInterfaceId = vpcops.createainit(b)
        print RouterInterfaceId
        result = {'RouterInterfaceId': RouterInterfaceId, 'result_message': 'success'}
        output = json.dumps(result)
        return output
    else:
        return '<h1>post</h1>'

@app.route('/updateaccept', methods=["POST","GET"])
def updateaccept():
    if request.method == 'GET':
        mydict = {}
        return render_template('updateAccept.html',mydict=mydict)
    if request.method == 'POST':
        a = request.get_data()
        b = json.loads(a)
        response_dict = vpcops.updateaccept(b)

        response_dict['result_message']='successfuly created'
        print response_dict
        output_json_str = json.dumps(response_dict)
        return Response(output_json_str, mimetype='application/json')
        # return jsonify(t)
    else:
        return '<h1>post</h1>'


# @app.route('/query',methods=["POST"])
# def create():
#


if __name__ == '__main__':
    app.run(
        host='127.0.0.1'
    )