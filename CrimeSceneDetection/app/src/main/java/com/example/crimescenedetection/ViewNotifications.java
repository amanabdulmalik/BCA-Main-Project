package com.example.crimescenedetection;

import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
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

public class ViewNotifications extends AppCompatActivity {
    ListView li;
    ArrayList<String> subject,content,date;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_notifications);
        li=(ListView)findViewById(R.id.list);

        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String ip=sh.getString("ip", "");
        String url = "http://" + ip + ":5000/and_view_notification";


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

                                subject=new ArrayList<>();
                                content=new ArrayList<>();
                                date=new ArrayList<>();

                                for(int i=0;i<jsa.length();i++)
                                {
                                    JSONObject jsob=jsa.getJSONObject(i);
                                    subject.add(jsob.getString("subject"));
                                    content.add(jsob.getString("content"));
                                    date.add(jsob.getString("notification_date"));

                                }

                                li.setAdapter(new CustomNotification(getApplicationContext(),date,subject,content));
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
    }
}
