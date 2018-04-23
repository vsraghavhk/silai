package io.github.vsraghavhk.silai.ui;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.support.annotation.NonNull;
import android.support.design.widget.NavigationView;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.widget.Toolbar;
import android.view.MenuItem;
import android.view.View;

import io.github.vsraghavhk.silai.R;

public abstract class BaseDrawerActivity extends BaseActivity {

    private static final int DRAWER_CLOSE_DELAY = 200;

    private Handler handler;

    private DrawerLayout drawerLayout;
    private NavigationView navigationView;
    private Toolbar toolbar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        handler = new Handler();
    }

    protected void setupDrawer() {
        drawerLayout = findViewById(R.id.drawer_layout);
        navigationView = findViewById(R.id.navigation_view);
        toolbar = findViewById(R.id.toolbar);
        navigationView.setNavigationItemSelectedListener(new NavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                onDrawerItemClicked(item.getItemId());
                return false;
            }
        });
    }

    protected void setDrawerIndicatorEnabled() {
        toolbar.setNavigationIcon(R.drawable.ic_drawer_light);
        toolbar.setContentDescription(getString(R.string.cd_open_drawer));
    }

    private void onDrawerItemClicked(int itemId) {
        Intent intent = null;
        launchCorrespondingActivity(intent);
        closeDrawer();
    }

    private void launchCorrespondingActivity(final Intent intent) {
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                startActivity(intent);
            }
        }, DRAWER_CLOSE_DELAY);
    }

    protected void setSelectedDrawerItem(int itemId) {
        navigationView.setCheckedItem(itemId);
    }

    protected boolean isDrawerOpen() {
        return drawerLayout.isDrawerOpen(navigationView);
    }

    protected void openDrawer() {
        drawerLayout.openDrawer(navigationView);
    }

    protected void closeDrawer() {
        drawerLayout.closeDrawer(navigationView);
    }

    protected boolean toggleDrawer(MenuItem item) {
        if (item != null && item.getItemId() == android.R.id.home) {
            if (drawerLayout.isDrawerVisible(navigationView)) {
                closeDrawer();
            } else {
                openDrawer();
            }
            return true;
        }
        return false;
    }

    protected View getSnackbarParentView() {
        return findViewById(android.R.id.content);
    }
}
