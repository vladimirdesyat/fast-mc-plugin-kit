package me.Author.Example;

import org.bukkit.event.Listener;
import org.bukkit.plugin.java.JavaPlugin;

public class Example extends JavaPlugin implements Listener {
    // placeholder
    @Override
    public void onEnable() {
        getServer().getPluginManager().registerEvents(this, this);
        getLogger().info("Example enabled!");
    }

    @Override
    public void onDisable() {
        getLogger().info("Example disabled!");
    }
}