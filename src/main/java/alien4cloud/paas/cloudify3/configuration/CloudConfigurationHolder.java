package alien4cloud.paas.cloudify3.configuration;

import java.util.List;

import javax.annotation.Resource;

import lombok.Setter;
import lombok.extern.slf4j.Slf4j;

import org.springframework.stereotype.Component;

import alien4cloud.paas.cloudify3.restclient.VersionClient;
import alien4cloud.paas.cloudify3.error.BadConfigurationException;
import alien4cloud.paas.cloudify3.model.Version;
import alien4cloud.paas.exception.PluginConfigurationException;

import com.google.common.collect.Lists;

@Component("cloudify-configuration-holder")
@Slf4j
public class CloudConfigurationHolder {

    private CloudConfiguration configuration;

    @Resource
    @Setter
    private VersionClient versionClient;

    private List<ICloudConfigurationChangeListener> listeners = Lists.newArrayList();

    public CloudConfigurationHolder() {
        this.registerListener(new ICloudConfigurationChangeListener() {
            @Override
            public void onConfigurationChange(CloudConfiguration newConfiguration) throws Exception {
                Version version = versionClient.read();
                log.info("Configure PaaS provider for Cloudify version " + version.getVersion());
            }
        });
    }

    public CloudConfiguration getConfiguration() {
        if (configuration == null) {
            throw new BadConfigurationException("Plugin is not properly configured");
        } else {
            return configuration;
        }
    }

    public synchronized void setConfiguration(CloudConfiguration configuration) throws PluginConfigurationException {
        this.configuration = configuration;
        try {
            for (ICloudConfigurationChangeListener listener : listeners) {
                listener.onConfigurationChange(configuration);
            }
        } catch (Exception e) {
            log.error("Cloud configuration is not correct", e);
            throw new PluginConfigurationException("Cloud configuration is not correct", e);
        }
    }

    public synchronized void registerListener(ICloudConfigurationChangeListener listener) {
        this.listeners.add(listener);
    }
}
