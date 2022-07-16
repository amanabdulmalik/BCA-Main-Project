package com.example.crimescenedetection;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ViewCriminals extends AppCompatActivity {

    ListView l1;
    public static ArrayList<String> name,gender,dob,bgroup,iden_marks,house_no,street,place,post,pin,district,father,mother,crime,photo;
    public static int pos=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_criminals);
        l1=(ListView)findViewById(R.id.list);



        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        String hu = sh.getString("ip", "");
        String url = "http://" + hu + ":5000/and_view_criminals";


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

                                name=new ArrayList<>();
                                gender=new ArrayList<>();
                                dob=new ArrayList<>();
                                bgroup=new ArrayList<>();
                                iden_marks=new ArrayList<>();
                                house_no=new ArrayList<>();
                                street=new ArrayList<>();
                                place=new ArrayList<>();
                                post=new ArrayList<>();
                                pin=new ArrayList<>();
                                district=new ArrayList<>();
                                father=new ArrayList<>();
                                mother=new ArrayList<>();
                                crime=new ArrayList<>();
                                photo=new ArrayList<>();

                                JSONArray ja=jsonObj.getJSONArray("data");

                                for(int i=0;i<ja.length();i++) {
                                    JSONObject jo = ja.getJSONObject(i);
                                    name.add(jo.getString("name"));
                                    gender.add(jo.getString("gender"));
                                    dob.add(jo.getString("dob"));
                                    bgroup.add(jo.getString("blood_group"));
                                    iden_marks.add(jo.getString("identification_marks"));
                                    house_no.add(jo.getString("house_no"));
                                    street.add(jo.getString("street"));
                                    place.add(jo.getString("place"));
                                    post.add(jo.getString("post"));
                                    pin.add(jo.getString("pin"));
                                    district.add(jo.getString("district"));
                                    father.add(jo.getString("father"));
                                    mother.add(jo.getString("mother"));
//                                    crime.add(jo.getString("crime"));
                                    photo.add(jo.getString("photo"));

                                }

                                l1.setAdapter(new CustomCriminal(getApplicationContext(),name,dob,place,district,photo));
                            }
                            else {
                                Toast.makeText(getApplicationContext(), "no complaints...", Toast.LENGTH_LONG).show();
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

                params.put("lid",sh.getString("lid",""));
                return params;
            }
        };

        int MY_SOCKET_TIMEOUT_MS = 100000;

        postRequest.setRetryPolicy(new DefaultRetryPolicy(
                MY_SOCKET_TIMEOUT_MS,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        requestQueue.add(postRequest);

        //l1.setOnItemClickListener(this);
    }
//
//    @Override
//    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
//
//        pos=i;
//        startActivity(new Intent(getApplicationContext(),ViewCriminal.class));
//    }
}
