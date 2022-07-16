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

public class ViewMissingPerson extends AppCompatActivity implements View.OnClickListener {
    ImageView im;
    TextView b;
    TextView t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_missing_person);
        im=(ImageView)findViewById(R.id.imageView2);
        b=(TextView) findViewById(R.id.button2);
        t1=(TextView)findViewById(R.id.name);
        t2=(TextView)findViewById(R.id.gender);
        t3=(TextView)findViewById(R.id.dob);
        t4=(TextView)findViewById(R.id.hno);
        t5=(TextView)findViewById(R.id.street);
        t6=(TextView)findViewById(R.id.city);
        t7=(TextView)findViewById(R.id.district);
        t8=(TextView)findViewById(R.id.state);
        t9=(TextView)findViewById(R.id.height);
        t10=(TextView)findViewById(R.id.weight);
        t11=(TextView)findViewById(R.id.skin);
        t12=(TextView)findViewById(R.id.iden);
        t13=(TextView)findViewById(R.id.missing);
        t14=(TextView)findViewById(R.id.last);
        t15=(TextView)findViewById(R.id.dress);
        t16=(TextView)findViewById(R.id.contact);


        t1.setText(ViewMissingPersons.name.get(ViewMissingPersons.pos));
        t2.setText(ViewMissingPersons.gender.get(ViewMissingPersons.pos));
        t3.setText(ViewMissingPersons.dob.get(ViewMissingPersons.pos));
        t4.setText(ViewMissingPersons.hno.get(ViewMissingPersons.pos));
        t5.setText(ViewMissingPersons.street.get(ViewMissingPersons.pos));
        t6.setText(ViewMissingPersons.city.get(ViewMissingPersons.pos));
        t7.setText(ViewMissingPersons.district.get(ViewMissingPersons.pos));
        t8.setText(ViewMissingPersons.state.get(ViewMissingPersons.pos));
        t9.setText(ViewMissingPersons.height.get(ViewMissingPersons.pos));
        t10.setText(ViewMissingPersons.weight.get(ViewMissingPersons.pos));
        t11.setText(ViewMissingPersons.skin_tone.get(ViewMissingPersons.pos));
        t12.setText(ViewMissingPersons.identification_mark.get(ViewMissingPersons.pos));
        t13.setText(ViewMissingPersons.missing_place.get(ViewMissingPersons.pos));
        t14.setText(ViewMissingPersons.last_sceen.get(ViewMissingPersons.pos));
        t15.setText(ViewMissingPersons.dress.get(ViewMissingPersons.pos));
        t16.setText(ViewMissingPersons.contact.get(ViewMissingPersons.pos));
        try
        {
            SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String url = "http://" + sh.getString("ip","") + ":5000/static/uploads/"+ViewMissingPersons.photo.get(ViewMissingPersons.pos);
            Picasso.with(getApplicationContext()).load(url).memoryPolicy(MemoryPolicy.NO_CACHE).networkPolicy(NetworkPolicy.NO_CACHE).transform(new CircleTransform()).error(R.drawable.ic_menu_gallery).into(im);

        }catch (Exception e)
        {
        }
        b.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {

        startActivity(new Intent(getApplicationContext(),ReportMissingPerson.class));
    }
}
