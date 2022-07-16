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

public class ViewMissingPersons extends AppCompatActivity implements AdapterView.OnItemClickListener {

    public static ArrayList<String> mid,name,gender,dob,photo,hno,street,city,district,state,height,weight,skin_tone,identification_mark,missing_place,last_sceen,dress,contact;
    public static int pos=0;
    ListView list;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_missing_persons);
        list=(ListView)findViewById(R.id.list);


        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String ip=sh.getString("ip", "");
        String url = "http://" + ip + ":5000/and_view_missingperson";


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


                                JSONArray jsa=jsonObj.getJSONArray("data");

                                mid=new ArrayList<>();
                                name=new ArrayList<>();
                                gender=new ArrayList<>();
                                dob=new ArrayList<>();
                                photo=new ArrayList<>();
                                hno=new ArrayList<>();
                                street=new ArrayList<>();
                                city=new ArrayList<>();
                                district=new ArrayList<>();
                                state=new ArrayList<>();
                                height=new ArrayList<>();
                                weight=new ArrayList<>();
                                skin_tone=new ArrayList<>();
                                identification_mark=new ArrayList<>();
                                missing_place=new ArrayList<>();
                                last_sceen=new ArrayList<>();
                                dress=new ArrayList<>();
                                contact=new ArrayList<>();
                                for(int i=0;i<jsa.length();i++)
                                {
                                    JSONObject jsob=jsa.getJSONObject(i);
                                    mid.add(jsob.getString("missing_id"));
                                    name.add(jsob.getString("name"));
                                    gender.add(jsob.getString("gender"));
                                    dob.add(jsob.getString("dob"));
                                    photo.add(jsob.getString("photo"));
                                    hno.add(jsob.getString("house_no"));
                                    street.add(jsob.getString("street"));
                                    city.add(jsob.getString("city"));
                                    district.add(jsob.getString("district"));
                                    state.add(jsob.getString("state"));
                                    height.add(jsob.getString("height"));
                                    weight.add(jsob.getString("weight"));
                                    skin_tone.add(jsob.getString("skin_tone"));
                                    identification_mark.add(jsob.getString("identification_marks"));
                                    missing_place.add(jsob.getString("missing_place"));
                                    last_sceen.add(jsob.getString("last_seen"));
                                    dress.add(jsob.getString("dress"));
                                    contact.add(jsob.getString("contact"));




                                }

                                list.setAdapter(new CustomMissing(getApplicationContext(),name,dob,missing_place,contact,photo));
//
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
        list.setOnItemClickListener(this);

    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        pos=i;
        startActivity(new Intent(getApplicationContext(),ViewMissingPerson.class));
    }
}
