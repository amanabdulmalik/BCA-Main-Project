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

public class ViewPoliceStations extends AppCompatActivity implements AdapterView.OnItemClickListener {
    ListView li;
    public static ArrayList<String> name,place,post,pin,city,district,photo,email,phone,fax,pid;
    public static int pos=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_police_stations);
        li=(ListView)findViewById(R.id.list);

        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String ip=sh.getString("ip", "");
        String url = "http://" + ip + ":5000/and_view_police";


        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        //    Toast.makeText(getApplicationContext(),"hai",Toast.LENGTH_SHORT).show();
        StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>()
                {
                    @Override
                    public void onResponse(String response) {

                        //  Toast.makeText(getApplicationContext(),response,Toast.LENGTH_SHORT).show();


                        // response
                        try {
                            JSONObject jsonObj = new JSONObject(response);
                            String sucs=   jsonObj.getString("status");
                            if(sucs.equalsIgnoreCase("ok"))
                            {

                                name=new ArrayList<>();
                                place=new ArrayList<>();
                                post=new ArrayList<>();
                                pin=new ArrayList<>();
                                city=new ArrayList<>();
                                district=new ArrayList<>();
                                photo=new ArrayList<>();
                                email=new ArrayList<>();
                                phone=new ArrayList<>();
                                fax=new ArrayList<>();
                                pid=new ArrayList<>();
                                JSONArray jsa=jsonObj.getJSONArray("data");



                                for(int i=0;i<jsa.length();i++)
                                {
                                    JSONObject jo=jsa.getJSONObject(i);
                                    name.add(jo.getString("name"));
                                    place.add(jo.getString("place"));
                                    post.add(jo.getString("post"));
                                    pin.add(jo.getString("pin"));
                                    city.add(jo.getString("city"));
                                    district.add(jo.getString("district"));
                                    photo.add(jo.getString("photo"));
                                    email.add(jo.getString("email"));
                                    phone.add(jo.getString("phone"));
                                    fax.add(jo.getString("fax"));
                                    pid.add(jo.getString("p_id"));
                                }

                                li.setAdapter(new CustomPoliceStation(getApplicationContext(),name,district,phone,email,photo));

                            }
                        } catch (Exception e) {
                            Toast.makeText(getApplicationContext(),"eeeee"+e.toString(),Toast.LENGTH_LONG).show();
                        }
                    }
                },
                new Response.ErrorListener()
                {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error
                        Toast.makeText(getApplicationContext(),"eeeee"+error.toString(),Toast.LENGTH_SHORT).show();
                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams()
            {
                SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                Map<String, String> params = new HashMap<String, String>();



                return params;
            }
        };

        requestQueue.add(postRequest);

        li.setOnItemClickListener(this);
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        pos=i;
        startActivity(new Intent(getApplicationContext(),ViewPoliceStation.class));
    }
}
