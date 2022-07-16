package com.example.crimescenedetection;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
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

public class ChangePassword extends AppCompatActivity implements View.OnClickListener {

    EditText ed1,ed2,ed3;
    Button b;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_change_password);

        ed1=(EditText)findViewById(R.id.editText2);
        ed2=(EditText)findViewById(R.id.editText14);
        ed3=(EditText)findViewById(R.id.editText15);
        b=(Button)findViewById(R.id.button8);

        b.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {


        final String curp=ed1.getText().toString();
        final String newp=ed2.getText().toString();
        String confp=ed3.getText().toString();

        int flag=0;
        if(curp.equals("")){
            flag++;
            ed1.setError("enter current password");
        }
        if(newp.length()<6){
            flag++;
            ed2.setError("password minimum 6 digits");
        }
        if(!newp.equals(confp)){
            flag++;
            ed3.setError("password not matching");
        }

        if(flag==0){
            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

            String hu = sh.getString("ip", "");
            String url = "http://" + hu + ":5000/change_password";


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

                                    Toast.makeText(ChangePassword.this, "success", Toast.LENGTH_SHORT).show();

                                    Intent ij = new Intent(getApplicationContext(), MainActivity.class);
                                    startActivity(ij);


                                } else if (jsonObj.getString("status").equalsIgnoreCase("no")) {
                                    Toast.makeText(getApplicationContext(), "Invalid  current password", Toast.LENGTH_LONG).show();
                                }


                                // }
                                else {
                                    Toast.makeText(getApplicationContext(), "Not found", Toast.LENGTH_LONG).show();
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
                    params.put("lid", sh.getString("lid",""));
                    params.put("npass", newp);
                    params.put("cpass",curp);


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
