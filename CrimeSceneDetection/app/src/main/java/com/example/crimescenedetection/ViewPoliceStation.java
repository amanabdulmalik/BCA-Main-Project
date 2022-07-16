package com.example.crimescenedetection;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.MemoryPolicy;
import com.squareup.picasso.NetworkPolicy;
import com.squareup.picasso.Picasso;

public class ViewPoliceStation extends AppCompatActivity implements View.OnClickListener {
    ImageView im;
    TextView t1,t2,t3,t4,t5,t6,t7,t8,t9;
    Button b;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_police_station);
        b=(Button)findViewById(R.id.button6);
        im=(ImageView)findViewById(R.id.imageView);
        t1=(TextView)findViewById(R.id.name);
        t2=(TextView)findViewById(R.id.place);
        t3=(TextView)findViewById(R.id.post);
        t4=(TextView)findViewById(R.id.pin);
        t5=(TextView)findViewById(R.id.city);
        t6=(TextView)findViewById(R.id.district);
        t7=(TextView)findViewById(R.id.email);
        t8=(TextView)findViewById(R.id.phone);
        t9=(TextView)findViewById(R.id.fax);
        b.setOnClickListener(this);


        t1.setText(ViewPoliceStations.name.get(ViewPoliceStations.pos));
        t2.setText(ViewPoliceStations.place.get(ViewPoliceStations.pos));
        t3.setText(ViewPoliceStations.post.get(ViewPoliceStations.pos));
        t4.setText(ViewPoliceStations.pin.get(ViewPoliceStations.pos));
        t5.setText(ViewPoliceStations.city.get(ViewPoliceStations.pos));
        t6.setText(ViewPoliceStations.district.get(ViewPoliceStations.pos));
        t7.setText(ViewPoliceStations.email.get(ViewPoliceStations.pos));
        t8.setText(ViewPoliceStations.phone.get(ViewPoliceStations.pos));
        t9.setText(ViewPoliceStations.fax.get(ViewPoliceStations.pos));
        try
        {
            SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String url = "http://" + sh.getString("ip","") + ":5000/static/uploads/"+ViewPoliceStations.photo.get(ViewPoliceStations.pos);
            Picasso.with(getApplicationContext()).load(url).memoryPolicy(MemoryPolicy.NO_CACHE).networkPolicy(NetworkPolicy.NO_CACHE).transform(new CircleTransform()).error(R.drawable.ic_menu_gallery).into(im);

        }catch (Exception e)
        {
        }
    }

    @Override
    public void onClick(View v) {
        String id=ViewPoliceStations.pid.get(ViewPoliceStations.pos);
        SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        SharedPreferences.Editor ed=sh.edit();
        ed.putString("toid",id);
        ed.commit();
        Intent ij=new Intent(getApplicationContext(),Test.class);
        startActivity(ij);
    }
}
