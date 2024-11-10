from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
app = Flask(__name__)

# Load the model at the start of the application
model = joblib.load("LSTM.pkl")  # Replace with your actual model path
featuress=['duration',
 'src_bytes',
 'dst_bytes',
 'land',
 'wrong_fragment',
 'urgent',
 'hot',
 'num_failed_logins',
 'logged_in',
 'num_compromised',
 'root_shell',
 'su_attempted',
 'num_root',
 'num_file_creations',
 'num_shells',
 'num_access_files',
 'num_outbound_cmds',
 'is_host_login',
 'is_guest_login',
 'count',
 'srv_count',
 'serror_rate',
 'srv_serror_rate',
 'rerror_rate',
 'srv_rerror_rate',
 'same_srv_rate',
 'diff_srv_rate',
 'srv_diff_host_rate',
 'dst_host_count',
 'dst_host_srv_count',
 'dst_host_same_srv_rate',
 'dst_host_diff_srv_rate',
 'dst_host_same_src_port_rate',
 'dst_host_srv_diff_host_rate',
 'dst_host_serror_rate',
 'dst_host_srv_serror_rate',
 'dst_host_rerror_rate',
 'dst_host_srv_rerror_rate',
 'intrusion',
 'icmp',
 'tcp',
 'udp',
 'IRC',
 'X11',
 'Z39_50',
 'aol',
 'auth',
 'bgp',
 'courier',
 'csnet_ns',
 'ctf',
 'daytime',
 'discard',
 'domain',
 'domain_u',
 'echo',
 'eco_i',
 'ecr_i',
 'efs',
 'exec',
 'finger',
 'ftp',
 'ftp_data',
 'gopher',
 'harvest',
 'hostnames',
 'http',
 'http_2784',
 'http_443',
 'http_8001',
 'imap4',
 'iso_tsap',
 'klogin',
 'kshell',
 'ldap',
 'link',
 'login',
 'mtp',
 'name',
 'netbios_dgm',
 'netbios_ns',
 'netbios_ssn',
 'netstat',
 'nnsp',
 'nntp',
 'ntp_u',
 'other',
 'pm_dump',
 'pop_2',
 'pop_3',
 'printer',
 'private',
 'red_i',
 'remote_job',
 'rje',
 'shell',
 'smtp',
 'sql_net',
 'ssh',
 'sunrpc',
 'supdup',
 'systat',
 'telnet',
 'tftp_u',
 'tim_i',
 'time',
 'urh_i',
 'urp_i',
 'uucp',
 'uucp_path',
 'vmnet',
 'whois',
 'OTH',
 'REJ',
 'RSTO',
 'RSTOS0',
 'RSTR',
 'S0',
 'S1',
 'S2',
 'S3',
 'SF',
 'SH']
def preprocess_data(data):
    df = pd.DataFrame(data,index=[0])
    std_scaler = StandardScaler()
    def standardization(df,col):
        for i in col:
            arr = df[i]
            arr = np.array(arr)
            df[i] = std_scaler.fit_transform(arr.reshape(len(arr),1))
        return df
    
    numeric_col = df.select_dtypes(include='number').columns
    df = standardization(df,numeric_col)
    df = pd.get_dummies(df,columns=['protocol_type','service','flag'],prefix="",prefix_sep="") 
    zero_float_dataset = pd.DataFrame(0.0, columns=featuress, index=range(len(df)))
    df = df.astype(int)
    df = df.astype(float)
    zero_float_dataset.update(df) 
    zero_float_dataset= zero_float_dataset.drop(labels=['intrusion'], axis=1)
    zero_float_dataset = np.reshape(zero_float_dataset, ( zero_float_dataset.shape[0], 1 , zero_float_dataset.shape[1] ))
    zero_float_dataset = zero_float_dataset.astype(np.float32)
    # Here you can add any preprocessing steps you need
    # Convert data to numpy array or process as required by your model
    return zero_float_dataset 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Preprocess the data
        processed_data = preprocess_data(data)

        # Make prediction
        prediction = model.predict([processed_data])
        max_index = np.argmax(prediction)
    # If the index is not 1, adjust it to be 1
        pred= 1 if max_index != 1 else max_index
        # Return the prediction result as JSON
        return jsonify({'prediction': pred})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
