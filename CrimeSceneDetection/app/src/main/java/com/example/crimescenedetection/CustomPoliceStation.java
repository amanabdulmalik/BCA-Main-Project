package com.example.crimescenedetection;

import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.MemoryPolicy;
import com.squareup.picasso.NetworkPolicy;
import com.squareup.picasso.Picasso;

import java.util.ArrayList;

public class CustomPoliceStation extends BaseAdapter {



    private android.content.Context Context;
    ArrayList<String> a;
    ArrayList<String> b;
    ArrayList<String> c;
    ArrayList<String> d;
    ArrayList<String> e;

    public CustomPoliceStation(android.content.Context applicationContext, ArrayList<String> a, ArrayList<String> b, ArrayList<String> c, ArrayList<String> d, ArrayList<String> e) {

        this.Context=applicationContext;
        this.a=a;
        this.b=b;
        this.c=c;
        this.d=d;
        this.e=e;

    }

    @Override
    public int getCount() {

        return a.size();
    }

    @Override
    public Object getItem(int arg0) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public long getItemId(int arg0) {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public View getView(int position, View convertview, ViewGroup parent) {


        LayoutInflater inflator=(LayoutInflater) Context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(convertview==null)
        {
            gridView=new View(Context);
            gridView=inflator.inflate(R.layout.custom_police_station, null);

        }
        else
        {
            gridView=(View)convertview;

        }

        TextView tv1=(TextView)gridView.findViewById(R.id.t1);
        TextView tv2=(TextView)gridView.findViewById(R.id.t2);
        TextView tv3=(TextView)gridView.findViewById(R.id.t3);
        TextView tv4=(TextView)gridView.findViewById(R.id.t4);
        ImageView img=(ImageView)gridView.findViewById(R.id.img);


        tv1.setTextColor(Color.BLACK);
        tv2.setTextColor(Color.BLACK);
        tv3.setTextColor(Color.BLACK);
        tv4.setTextColor(Color.BLACK);


        tv1.setText(a.get(position));
        tv2.setText(b.get(position));
        tv3.setText(c.get(position));
        tv4.setText(d.get(position));
        try
        {
            SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(Context);
            String url = "http://" + sh.getString("ip","") + ":5000/static/uploads/"+e.get(position);
            Picasso.with(Context).load(url).memoryPolicy(MemoryPolicy.NO_CACHE).networkPolicy(NetworkPolicy.NO_CACHE).transform(new CircleTransform()).error(R.drawable.ic_menu_gallery).into(img);

        }catch (Exception e)
        {
        }

        return gridView;
    }

}