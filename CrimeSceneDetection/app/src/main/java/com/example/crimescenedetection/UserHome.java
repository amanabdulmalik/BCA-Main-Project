package com.example.crimescenedetection;

import android.content.Intent;
import android.os.Bundle;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;
import android.view.View;
import androidx.core.view.GravityCompat;
import androidx.appcompat.app.ActionBarDrawerToggle;
import android.view.MenuItem;
import com.google.android.material.navigation.NavigationView;
import androidx.drawerlayout.widget.DrawerLayout;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import android.view.Menu;

public class UserHome extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_home);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        NavigationView navigationView = findViewById(R.id.nav_view);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();
        navigationView.setNavigationItemSelectedListener(this);
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

//    @Override
//    public boolean onCreateOptionsMenu(Menu menu) {
//        // Inflate the menu; this adds items to the action bar if it is present.
//        getMenuInflater().inflate(R.menu.user_home, menu);
//        return true;
//    }
//
//    @Override
//    public boolean onOptionsItemSelected(MenuItem item) {
//        // Handle action bar item clicks here. The action bar will
//        // automatically handle clicks on the Home/Up button, so long
//        // as you specify a parent activity in AndroidManifest.xml.
//        int id = item.getItemId();
//
//        //noinspection SimplifiableIfStatement
//        if (id == R.id.action_settings) {
//            return true;
//        }
//
//        return super.onOptionsItemSelected(item);
//    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_lookout) {
            Intent lookout=new Intent(getApplicationContext(),ViewLookout.class);
            startActivity(lookout);

        } else if (id == R.id.nav_missing) {
            Intent missing=new Intent(getApplicationContext(),ViewMissingPersons.class);
            startActivity(missing);

        } else if (id == R.id.nav_criminals) {
            Intent criminals=new Intent(getApplicationContext(),ViewCriminals.class);
            startActivity(criminals);

        } else if (id == R.id.nav_police) {
            Intent police=new Intent(getApplicationContext(),ViewPoliceStations.class);
            startActivity(police);

        }else if (id == R.id.nav_replies) {
            Intent replies=new Intent(getApplicationContext(),ViewComplaintReply.class);
            startActivity(replies);

        }else if (id == R.id.nav_notifications){
            Intent notification=new Intent(getApplicationContext(),ViewNotifications.class);
            startActivity(notification);

        } else if (id == R.id.nav_share) {
            Intent notification=new Intent(getApplicationContext(),ChangePassword.class);
            startActivity(notification);
        } else if (id == R.id.nav_send) {
            Intent notification=new Intent(getApplicationContext(),MainActivity.class);
            startActivity(notification);
        }

        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
