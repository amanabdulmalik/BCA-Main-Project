package com.example.crimescenedetection;

import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.MemoryPolicy;
import com.squareup.picasso.NetworkPolicy;
import com.squareup.picasso.Picasso;

public class ViewCriminal extends AppCompatActivity {
    ImageView im;
    TextView t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_criminal);
        im=(ImageView)findViewById(R.id.imageView2);
        t1=(TextView)findViewById(R.id.name);
        t2=(TextView)findViewById(R.id.gender);
        t3=(TextView)findViewById(R.id.dob);
        t4=(TextView)findViewById(R.id.bgroup);
        t5=(TextView)findViewById(R.id.iden);
        t6=(TextView)findViewById(R.id.hno);
        t7=(TextView)findViewById(R.id.street);
        t8=(TextView)findViewById(R.id.place);
        t9=(TextView)findViewById(R.id.post);
        t10=(TextView)findViewById(R.id.pin);
        t11=(TextView)findViewById(R.id.district);
        t12=(TextView)findViewById(R.id.fname);
        t13=(TextView)findViewById(R.id.mname);
        t14=(TextView)findViewById(R.id.crime);


        t1.setText(ViewCriminals.name.get(ViewCriminals.pos));
        t2.setText(ViewCriminals.gender.get(ViewCriminals.pos));
        t3.setText(ViewCriminals.dob.get(ViewCriminals.pos));
        t4.setText(ViewCriminals.bgroup.get(ViewCriminals.pos));
        t5.setText(ViewCriminals.iden_marks.get(ViewCriminals.pos));
        t6.setText(ViewCriminals.house_no.get(ViewCriminals.pos));
        t7.setText(ViewCriminals.street.get(ViewCriminals.pos));
        t8.setText(ViewCriminals.place.get(ViewCriminals.pos));
        t9.setText(ViewCriminals.post.get(ViewCriminals.pos));
        t10.setText(ViewCriminals.pin.get(ViewCriminals.pos));
        t11.setText(ViewCriminals.district.get(ViewCriminals.pos));
        t12.setText(ViewCriminals.father.get(ViewCriminals.pos));
        t13.setText(ViewCriminals.mother.get(ViewCriminals.pos));
        t14.setText(ViewCriminals.crime.get(ViewCriminals.pos));

        try
        {
            SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String url = "http://" + sh.getString("ip","") + ":5000/static/uploads/"+ViewCriminals.photo.get(ViewCriminals.pos);
            Picasso.with(getApplicationContext()).load(url).memoryPolicy(MemoryPolicy.NO_CACHE).networkPolicy(NetworkPolicy.NO_CACHE).transform(new CircleTransform()).error(R.drawable.ic_menu_gallery).into(im);

        }catch (Exception e)
        {
        }
    }
}
