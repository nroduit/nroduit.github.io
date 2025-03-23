---
title: Build Plugins
keywords: [ "plugins", "weasis plugins", "dicom viewer", "free dicom viewer", "open source dicom viewer", "weasis dicom viewer",  "multi-platform dicom viewer", "dicom", "pacs", "pacs viewer" ]
description: How to build new Weasis plugins and how they can be incorporated to the distributions
weight: 30
---

## <center>How to build and install a plugin</center>

This page provides a guide on creating new Weasis plugins and explains how to integrate them into the distributions. For details on configuring the development environment, refer to this [guidelines page](../../../getting-started/guidelines).

### Types of Plugins in Weasis

The following list describes the types of plugins, the interfaces they implement and the factories they use:

1. **Media Viewer or Editor**
    - Represents the main central panel and implements either `ViewerPlugin` or `ImageViewerPlugin`.
    - The factory for this type implements `SeriesViewerFactory`.
    - For DICOM special modalities, you can use `DicomSpecialElementFactory` to associate a viewer to a specific DICOM object.
2. **Toolbar Associated with a Viewer**
    - Implements the `Toolbar` or `DynamicToolbar` interface.
    - The factory for this type implements `InsertableFactory`
3. **Tool Associated with a Viewer**
    - Represents the right panel and implements `DockableTool`.
    - The factory for this type implements `InsertableFactory`.
4. **Data Explorer**
    - The explorer model implements `DataExplorerModel`.
    - The explorer view implements `DataExplorerView`.
    - The factory for this type implements `DataExplorerViewFactory`.
5. **Import Data into an Explorer**
    - Adds a new page into the DICOM Import UI with `ImportDicom`.
    - The factory for this type implements `DicomImportFactory`.
6. **Export Data from an Explorer**
    - Adds a new page into the DICOM Export UI with `ExportDicom`
    - The factory for this type implements `DicomExportFactory`.
7. **Media Codec**
    - Implements the `Codec` interface to decode and encode media files related to a file extension or a mime type.
8. **Preferences**
    - Implements `PreferencesPageFactory` to add a new page in the Preferences dialog.
9. **UI Aggregator**
    - Represents the bundle for the application's main user interface which aggregates various interface components.
    - The Maven artifact for this bundle must be defined in the `base.json` file (e.g., code:`weasis.main.ui` value:`weasis-base-ui`).

{{% notice note %}}
The factories are used to create the instances of the plugins and are registered as OSGi services. For performance reasons, the factories are created at startup and the plugins are created only if they are needed.
{{% /notice %}}

{{% notice tip %}}
For more information about the plugin hierarchy and their relationships, refer to the [Weasis Architecture](../../architecture).
{{% /notice %}}

### Building Plugins Using Maven Archetype

1. To add the Weasis archetypes to your local Maven repository, go to the `Weasis/archetype` directory and execute the following command:
    ``` bash
       mvn install
    ```
2. Navigate to the target folder, which should be the parent folder of the new plugin project, and execute the following command to create your plugin:
    ``` bash
       mvn archetype:generate -DarchetypeCatalog=local
    ```
3. When prompted, enter the number of one of the archetypes. Currently, the following archetypes are available:
    - **`weasis-plugin-base-viewer-archetype`**: Example of a toolbar and tool for a non-DICOM viewer.
    - **`weasis-plugin-dicom-viewer-archetype`**: Example of a toolbar and tool for a DICOM viewer.
4. Modify the generated project as needed.
   - In the pom.xml file, ensure the `<relativePath>` tag corresponds to the location of your Weasis source folder. By default, the value is `<relativePath>../Weasis/weasis-parent/pom.xml</relativePath>` (In this scenario, the plugin resides in the same parent folder as the Weasis source code).
   - When the relative path is set correctly, `<version>${revision}${changelist}</version>` in the pom.xml file will automatically be updated to the latest version of the Weasis source.
   - For easier version management in the pom.xml, you can remove `<version>` at the project level to inherit it from the parent.
5. Build the plugin by executing the following command in the plugin project directory:
    ``` bash
       mvn clean install
    ```

### Integrating Plugins into Weasis Distributions

Once the plugin is built, it can be integrated into the Weasis distributions either locally or remotely.

{{% notice warning %}}
The plugin depends on the Weasis framework, and its version must align with the version of the Weasis distribution being integrated.<br>
If the versions do not match, the plugin may fail to start and produce an error such as _org.osgi.framework.BundleException: Unable to resolve myplugin ..._.
{{% /notice %}}

#### Testing the Plugin

To test the plugin with an installed version of Weasis without making any changes to the installed directory, create a JSON file that extends the configuration specified in [base.json](https://github.com/nroduit/Weasis/blob/master/weasis-distributions/etc/config/base.json). 

1. Create a new json file (e.g., `myplugin.json`) with the following content:
    ``` json
    {
      "weasisPreferences": [
        {
          "code": "org.osgi.framework.startlevel.beginning",
          "value": "550"
        },
        {
          "code": "felix.auto.start.500",
          "value": "file:///git/myplugin/target/myplugin-4.5.2.jar",
          "description": "Myplugin - a viewer for ..."
        }
      ]
    }
    ```
2. Update the content of `myplugin.json` as required:
    - Ensure the plugin start level (above 500) is lower than the OSGi beginning level (above 550). Avoid using values below this range to prevent conflicts with other plugins.
    - For easier testing, use an absolute JAR path that matches your local plugin directory. Use a URI format for the path like:
    {{< tabs groupid="launchPlugin">}}
      {{% tab title="Windows" %}}
      file:///D:/git/myplugin/target/myplugin-4.5.2.jar
      {{% /tab %}}
      {{% tab title="Linux" %}}
      file:///git/myplugin/target/myplugin-4.5.2.jar
      {{% /tab %}}
      {{% tab title="macOS" %}}
      file:///git/myplugin/target/myplugin-4.5.2.jar
      {{% /tab %}}
      {{< /tabs >}}
3. Launch Weasis with your configuration: 
    - Use the following parameter to extend the configuration (adapt the path to your local file):
      {{< tabs groupid="launchPlugin">}}
      {{% tab title="Windows" %}}
      $weasis:config pro="felix.extended.config.properties file:///D:/git/myplugin/myplugin.json"
      {{% /tab %}}
      {{% tab title="Linux" %}}
      $weasis:config pro="felix.extended.config.properties file:///git/myplugin/myplugin.json"
      {{% /tab %}}
      {{% tab title="macOS" %}}
      $weasis:config pro="felix.extended.config.properties file:///git/myplugin/myplugin.json"
      {{% /tab %}}
      {{< /tabs >}}
    - Build a valid URI with the above parameter (see [How to build an URI](../../../getting-started/weasis-protocol/#how-to-build-a-uri)) and launch Weasis from the command on a terminal:Construct a valid URI using the parameter mentioned above (refer to [How to build a URI](../../../getting-started/weasis-protocol/#how-to-build-a-uri))) and launch Weasis from the terminal using a command:
      {{< tabs groupid="launchPlugin">}}
      {{% tab title="Windows" %}}
      start weasis://?%24weasis%3Aconfig%20pro%3D%22felix.extended.config.properties%20file%3A%2F%2F%2FD%3A%2Fgit%2Fmyplugin%2Fmyplugin.json%22
      {{% /tab %}}
      {{% tab title="Linux" %}}
      xdg-open weasis://?%24weasis%3Aconfig%20pro%3D%22felix.extended.config.properties%20file%3A%2F%2F%2Fgit%2Fmyplugin%2Fmyplugin.json%22
      {{% /tab %}}
      {{% tab title="macOS" %}}
      open weasis://?%24weasis%3Aconfig%20pro%3D%22felix.extended.config.properties%20file%3A%2F%2F%2Fgit%2Fmyplugin%2Fmyplugin.json%22
      {{% /tab %}}
      {{< /tabs >}}


#### Using ViewerHub
This feature will be available soon. It will allow you to manage the plugins and their configurations directly from the ViewerHub web portal.

### Build OSGi Services

All the plugin type described in the list above are OSGi services that are registered and aggregated in the GUI. Building the plugin from the Maven archetype will configure the OSGi service automatically. For adding new OSGi services, here is the procedure:
1. Create a class that implements the `Insertable` interface and represents a visual component. For example:
    {{< highlight java >}}
    public class MyPrefView extends AbstractItemDialogPage {
    
       public MyPrefView() {
           super("My Preferences", 100); // Provide a name and the page position
           initGUI();
       }
    
       private void initGUI() {
           // Add a basic JLabel to the preference panel for demonstration
           add(new JLabel("Welcome to My Preferences!"));
       }
    
       @Override
       public void closeAdditionalWindow() {
           // Handle any cleanup or saving preferences when closing
       }
    
       @Override
       public void resetToDefaultValues() {
           // Reset preferences to default values
       }
    }
    {{< /highlight >}}

2. Create a class that implements one of the plugin factories and include the annotations `@Component` and the `@Service` parameter. For example:
{{< highlight java >}}
@org.osgi.service.component.annotations.Component(service = PreferencesPageFactory.class)
public class MyViewerPrefFactory implements PreferencesPageFactory {

    @Override
    public AbstractItemDialogPage createInstance(Hashtable<String, Object> properties) {
    return new MyPrefView();
    }
    
    @Override
    public boolean isComponentCreatedByThisFactory(Insertable component) {
    return component instanceof MyPrefView;
    }
}

{{< /highlight >}}
{{% notice tip %}} 
For more details on annotations, refer to the [Apache Felix SCR Annotations documentation](https://felix.apache.org/documentation/subprojects/apache-felix-maven-scr-plugin/scr-annotations.html).
{{% /notice %}}

