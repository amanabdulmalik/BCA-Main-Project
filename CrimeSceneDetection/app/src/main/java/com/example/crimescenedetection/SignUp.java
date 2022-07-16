package com.example.crimescenedetection;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class SignUp extends AppCompatActivity implements View.OnClickListener {
    EditText e1,e2,e3,e4,e5,e6,e7;
    RadioGroup rg;
    RadioButton r1,r2,r3;
    TextView t1,t2,t3;
    Button b;
    String gender="";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_up);
        e1=(EditText)findViewById(R.id.editText);
        e2=(EditText)findViewById(R.id.place);
        e3=(EditText)findViewById(R.id.pin);
        e4=(EditText)findViewById(R.id.email);
        e5=(EditText)findViewById(R.id.phone);
        e6=(EditText)findViewById(R.id.password);
        e7=(EditText)findViewById(R.id.cpassword);
        r1=(RadioButton)findViewById(R.id.radioButton);
        r2=(RadioButton)findViewById(R.id.radioButton2);
        r3=(RadioButton)findViewById(R.id.radioButton3);
        b=(Button)findViewById(R.id.button2);



        b.setOnClickListener(this);

    }

    @Override
    public void onClick(View view) {

        final String name=e1.getText().toString();
        final String place=e2.getText().toString();
        final String pin=e3.getText().toString();
        final String email=e4.getText().toString();
        final String phone=e5.getText().toString();
        final String password=e6.getText().toString();
        final String cpassword=e7.getText().toString();
        if(r1.isChecked()){
            gender="male";
        }
        else if(r2.isChecked()){

            gender="female";
        }
        else{

            gender="other";
        }
        int flag=0;
        if(name.equals("")){
            flag++;
            e1.setError("Enter name");
        }
        if(place.equals("")){
            flag++;
            e2.setError("Enter place");
        }
        if(pin.equals("")){
            flag++;
            e3.setError("Enter pin");
        }
        if(!Patterns.EMAIL_ADDRESS.matcher(email).matches()){
            flag++;
            e4.setError("Enter email address");
        }
        if(!Patterns.PHONE.matcher(phone).matches()){
            flag++;
            e5.setError("Enter phone");
        }
        if(password.length()<6){
            flag++;
            e6.setError("Password minimum 6 digits");
        }
        if(!cpassword.equals(password)){
            flag++;
            e7.setError("Password not matching");
        }


        if(flag==0) {
            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

            String hu = sh.getString("ip", "");
            String url = "http://" + hu + ":5000/and_user_reg";


            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            //  Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();

                            // response
                            try {
                                JSONObject jsonObj = new JSONObject(response);
                                 if (jsonObj.getString("status").equalsIgnoreCase("ok")) {
                                    Toast.makeText(getApplicationContext(), "Registration success..!!", Toast.LENGTH_LONG).show();
                                    startActivity(new Intent(getApplicationContext(),MainActivity.class));
                                }
                                else {
                                    Toast.makeText(getApplicationContext(), "something went wrong..! try again later", Toast.LENGTH_LONG).show();
                                }

                            } catch (Exception e) {
                                Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                            }
                        }
                    },
                    new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            // error
                            Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                        }
                    }
            ) {
                @Override
                protected Map<String, String> getParams() {
                    SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    Map<String, String> params = new HashMap<String, String>();

//                String id=sh.getString("uid","");
                    params.put("name", name);
                    params.put("place", place);
                    params.put("pin", pin);
                    params.put("gender", gender);
                    params.put("phone", phone);
                    params.put("email", email);
                    params.put("pswd", password);


                    return params;
                }
            };

            int MY_SOCKET_TIMEOUT_MS = 100000;

            postRequest.setRetryPolicy(new DefaultRetryPolicy(
                    MY_SOCKET_TIMEOUT_MS,
                    DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                    DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
            requestQueue.add(postRequest);
        }
    }
}
