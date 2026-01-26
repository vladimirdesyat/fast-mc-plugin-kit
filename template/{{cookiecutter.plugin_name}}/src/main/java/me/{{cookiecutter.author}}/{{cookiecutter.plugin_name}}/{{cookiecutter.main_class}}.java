package me.{{cookiecutter.author}}.{{cookiecutter.plugin_name}};

import org.bukkit.event.Listener;
import org.bukkit.plugin.java.JavaPlugin;

public class {{cookiecutter.main_class}} extends JavaPlugin implements Listener {
    // placeholder
    @Override
    public void onEnable() {
        getServer().getPluginManager().registerEvents(this, this);
        getLogger().info("{{cookiecutter.plugin_name}} enabled!");
    }

    @Override
    public void onDisable() {
        getLogger().info("{{cookiecutter.plugin_name}} disabled!");
    }
}