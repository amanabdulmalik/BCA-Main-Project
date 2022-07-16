package com.example.crimescenedetection;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.gms.common.GooglePlayServicesNotAvailableException;
import com.google.android.gms.common.GooglePlayServicesRepairableException;
import com.google.android.gms.location.places.Place;
import com.google.android.gms.location.places.ui.PlacePicker;
import com.google.android.gms.maps.model.LatLng;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class ReportMissingPerson extends AppCompatActivity implements View.OnClickListener {
    Button b;
    EditText e,e2;
    ImageView img;
    String latti=LocationService.lati;
    String longi=LocationService.logi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_report_missing_person);
        e=(EditText)findViewById(R.id.editText10);
        b=(Button)findViewById(R.id.button3);
        e2=(EditText)findViewById(R.id.place);
        img=(ImageView)findViewById(R.id.imageView4);
        e2.setText(LocationService.place);
        e2.setEnabled(false);
        e2.setText(LocationService.place);
        b.setOnClickListener(this);

        img.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {


                PlacePicker.IntentBuilder builder = new PlacePicker.IntentBuilder();
                try {
                    startActivityForResult(builder.build(ReportMissingPerson.this), 100);
                } catch (GooglePlayServicesRepairableException e) {
                    e.printStackTrace();
                } catch (GooglePlayServicesNotAvailableException e) {
                    e.printStackTrace();
                }

            }
        });
    }

    @Override
    public void onClick(View view) {

        final String info=e.getText().toString();
        final String place=e2.getText().toString();



        int flag=0;
        if(info.equals("")){
            e.setError("Enter information");
            flag++;
        }
        if(place.equals("")){
            e2.setError("location not available");
            flag++;
        }

        if(flag==0){
            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

            String hu = sh.getString("ip", "");
            String url = "http://" + hu + ":5000/and_missingpersonreporting";


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

                                    Toast.makeText(ReportMissingPerson.this, "success", Toast.LENGTH_SHORT).show();

                                    Intent ij = new Intent(getApplicationContext(), UserHome.class);
                                    startActivity(ij);


                                } else if (jsonObj.getString("status").equalsIgnoreCase("no")) {
                                    Toast.makeText(getApplicationContext(), "try again later", Toast.LENGTH_LONG).show();
                                }
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

                    params.put("lid", sh.getString("lid",""));
                    params.put("info", info);
                    params.put("place",place);
                    params.put("latti",latti);
                    params.put("longi",longi);
                    params.put("mid",ViewMissingPersons.mid.get(ViewMissingPersons.pos));


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

    protected void onActivityResult(int requestCode, int resultCode, Intent data) {

        if (requestCode == 100) {
            if (resultCode == RESULT_OK) {
                Place place = PlacePicker.getPlace(data, this);
                e2.setText(place.getName());
                LatLng latLng = place.getLatLng();
                latti = Double.toString(latLng.latitude);
                longi = Double.toString(latLng.longitude);
            }

        }

    }
}
