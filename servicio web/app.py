# Gema Correa Fernández

"""
Aplicación Web v0.1
"""

from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)


# ------------------------------------------------------------------------------


@app.route('/')
def index():

    '''
    Función que nos redirige a la página principal
    '''

    return render_template('index.html')


# ------------------------------------------------------------------------------


@app.route('/regresion_logistica')
def formulario_regresion_logistica():

    '''
    Función que nos redirige al formulario del modelo de Regresión Logística
    '''

    return render_template('formulario_regresion_logistica.html')


@app.route('/random_forest')
def formulario_random_forest():

    '''
    Función que nos redirige al formulario del modelo de Random Forest
    '''

    return render_template('formulario_random_forest.html')


@app.route('/gradient_boosting')
def formulario_gradient_boosting():

    '''
    Función que nos redirige al formulario del modelo de Gradient Boosting
    '''

    return render_template('formulario_gradient_boosting.html')


# ------------------------------------------------------------------------------


@app.route('/probabilidad_random_forest',  methods=['POST'])
def probabilidad_random_forest():

    '''
    Función que nos redirige a visualizar la probabilidad del algoritmo Random Forest
    '''

    ProductName = request.form.get("ProductName")
    EngineVersion = request.form.get("EngineVersion")
    AppVersion = request.form.get("AppVersion")
    IsBeta = request.form.get("IsBeta")
    IsSxsPassiveMode = request.form.get("IsSxsPassiveMode")
    AVProductsInstalled = request.form.get("AVProductsInstalled")
    AVProductsEnabled = request.form.get("AVProductsEnabled")
    HasTpm = request.form.get("HasTpm")
    CountryIdentifier = request.form.get("CountryIdentifier")
    CityIdentifier = request.form.get("CityIdentifier")
    OrganizationIdentifier = request.form.get("OrganizationIdentifier")
    LocaleEnglishNameIdentifier = request.form.get("LocaleEnglishNameIdentifier")
    Platform = request.form.get("Platform")
    Processor = request.form.get("Processor")
    OsBuild = request.form.get("OsBuild")
    OsSuite = request.form.get("OsSuite")
    OsPlatformSubRelease = request.form.get("OsPlatformSubRelease")
    IsProtected = request.form.get("IsProtected")
    SMode = request.form.get("SMode")
    IeVerIdentifier = request.form.get("IeVerIdentifier")
    SmartScreen = request.form.get("SmartScreen")
    Firewall = request.form.get("Firewall")
    UacLuaenable = request.form.get("UacLuaenable")
    Census_MDC2FormFactor = request.form.get("Census_MDC2FormFactor")
    Census_DeviceFamily = request.form.get("Census_DeviceFamily")
    Census_OEMNameIdentifier = request.form.get("Census_OEMNameIdentifier")
    Census_OEMModelIdentifier = request.form.get("Census_OEMModelIdentifier")
    Census_ProcessorCoreCount = request.form.get("Census_ProcessorCoreCount")
    Census_ProcessorManufacturerIdentifier = request.form.get("")
    Census_PrimaryDiskTypeName = request.form.get("Census_PrimaryDiskTypeName")
    Census_HasOpticalDiskDrive = request.form.get("Census_HasOpticalDiskDrive")
    Census_ChassisTypeName = request.form.get("Census_ChassisTypeName")
    Census_InternalPrimaryDiagonalDisplaySizeInInches = request.form.get("Census_InternalPrimaryDiagonalDisplaySizeInInches")
    Census_InternalPrimaryDisplayResolutionHorizontal = request.form.get("Census_InternalPrimaryDisplayResolutionHorizontal")
    Census_PowerPlatformRoleName = request.form.get("Census_PowerPlatformRoleName")
    Census_InternalBatteryNumberOfCharges = request.form.get("Census_InternalBatteryNumberOfCharges")
    Census_OSBuildRevision = request.form.get("Census_OSBuildRevision")
    Census_OSEdition = request.form.get("Census_OSEdition")
    Census_OSInstallTypeName = request.form.get("Census_OSInstallTypeName")
    Census_OSInstallLanguageIdentifier = request.form.get("Census_OSInstallLanguageIdentifier")
    Census_OSWUAutoUpdateOptionsName = request.form.get("Census_OSWUAutoUpdateOptionsName")
    Census_IsPortableOperatingSystem = request.form.get("Census_IsPortableOperatingSystem")
    Census_GenuineStateName = request.form.get("Census_GenuineStateName")
    Census_ActivationChannel = request.form.get("Census_ActivationChannel")
    Census_IsFlightsDisabled = request.form.get("Census_IsFlightsDisabled")
    Census_FlightRing = request.form.get("Census_FlightRing")
    Census_FirmwareManufacturerIdentifier = request.form.get("Census_FirmwareManufacturerIdentifier")
    Census_FirmwareVersionIdentifier = request.form.get("Census_FirmwareVersionIdentifier")
    Census_IsSecureBootEnabled = request.form.get("Census_IsSecureBootEnabled")
    Census_IsVirtualDevice = request.form.get("Census_IsVirtualDevice")
    Census_IsTouchEnabled = request.form.get("Census_IsTouchEnabled")
    Census_IsPenCapable = request.form.get("Census_IsPenCapable")
    Census_IsAlwaysOnAlwaysConnectedCapable = request.form.get("Census_IsAlwaysOnAlwaysConnectedCapable")
    Wdft_IsGamer = request.form.get("Wdft_IsGamer")
    Wdft_RegionIdentifier = request.form.get("Wdft_RegionIdentifier")
    Census_TotalPhysicalRAMGB = request.form.get("Census_TotalPhysicalRAMGB")
    Census_SystemVolumeTotalCapacityGB = request.form.get("Census_SystemVolumeTotalCapacityGB")
    Census_PrimaryDiskTotalCapacityGB = request.form.get("Census_PrimaryDiskTotalCapacityGB")

    # Cogemos los valores del de la petición POST (formato dicciones)
    f = request.form

    # Nos quedamos con las claves
    list_keys = []
    for key in f.keys():
        list_keys.append(key)
    print(list_keys)

    # Nos quedamos con los valores
    list_values = []
    for value in f.values():
        list_values.append(value)
    print(list_values)
    list_values = list(map(int, list_values))

    # Es necesario que el json esté en un formato adecuado
    # {"columns": ["alcohol", "chlorides", "citric_acid"], "data": [4, 4, 4]}
    print(json.dumps({"columns": list_keys, "data": [list_values]}))
    data = json.dumps({"columns": list_keys, "data": [list_values]})

    # Hacemos la petición, y nos quedamos con la salida (probabilidad)
    url = 'http://localhost:8001/invocations'
    headers = {"content-type": "application/json; format=pandas-split"}
    r = requests.post(url, data=data, headers=headers)

    return render_template("probabilidad_random_forest.html", malware = r.text)


@app.route('/probabilidad_regresion_logistica',  methods=['POST'])
def probabilidad_regresion_logistica():

    '''
    Función que nos redirige a visualizar la probabilidad del algoritmo Regresión Logística
    '''

    ProductName = request.form.get("ProductName")
    EngineVersion = request.form.get("EngineVersion")
    AppVersion = request.form.get("AppVersion")
    IsBeta = request.form.get("IsBeta")
    IsSxsPassiveMode = request.form.get("IsSxsPassiveMode")
    AVProductsInstalled = request.form.get("AVProductsInstalled")
    AVProductsEnabled = request.form.get("AVProductsEnabled")
    HasTpm = request.form.get("HasTpm")
    CountryIdentifier = request.form.get("CountryIdentifier")
    CityIdentifier = request.form.get("CityIdentifier")
    OrganizationIdentifier = request.form.get("OrganizationIdentifier")
    LocaleEnglishNameIdentifier = request.form.get("LocaleEnglishNameIdentifier")
    Platform = request.form.get("Platform")
    Processor = request.form.get("Processor")
    OsBuild = request.form.get("OsBuild")
    OsSuite = request.form.get("OsSuite")
    OsPlatformSubRelease = request.form.get("OsPlatformSubRelease")
    IsProtected = request.form.get("IsProtected")
    SMode = request.form.get("SMode")
    IeVerIdentifier = request.form.get("IeVerIdentifier")
    SmartScreen = request.form.get("SmartScreen")
    Firewall = request.form.get("Firewall")
    UacLuaenable = request.form.get("UacLuaenable")
    Census_MDC2FormFactor = request.form.get("Census_MDC2FormFactor")
    Census_DeviceFamily = request.form.get("Census_DeviceFamily")
    Census_OEMNameIdentifier = request.form.get("Census_OEMNameIdentifier")
    Census_OEMModelIdentifier = request.form.get("Census_OEMModelIdentifier")
    Census_ProcessorCoreCount = request.form.get("Census_ProcessorCoreCount")
    Census_ProcessorManufacturerIdentifier = request.form.get("")
    Census_PrimaryDiskTypeName = request.form.get("Census_PrimaryDiskTypeName")
    Census_HasOpticalDiskDrive = request.form.get("Census_HasOpticalDiskDrive")
    Census_ChassisTypeName = request.form.get("Census_ChassisTypeName")
    Census_InternalPrimaryDiagonalDisplaySizeInInches = request.form.get("Census_InternalPrimaryDiagonalDisplaySizeInInches")
    Census_InternalPrimaryDisplayResolutionHorizontal = request.form.get("Census_InternalPrimaryDisplayResolutionHorizontal")
    Census_PowerPlatformRoleName = request.form.get("Census_PowerPlatformRoleName")
    Census_InternalBatteryNumberOfCharges = request.form.get("Census_InternalBatteryNumberOfCharges")
    Census_OSBuildRevision = request.form.get("Census_OSBuildRevision")
    Census_OSEdition = request.form.get("Census_OSEdition")
    Census_OSInstallTypeName = request.form.get("Census_OSInstallTypeName")
    Census_OSInstallLanguageIdentifier = request.form.get("Census_OSInstallLanguageIdentifier")
    Census_OSWUAutoUpdateOptionsName = request.form.get("Census_OSWUAutoUpdateOptionsName")
    Census_IsPortableOperatingSystem = request.form.get("Census_IsPortableOperatingSystem")
    Census_GenuineStateName = request.form.get("Census_GenuineStateName")
    Census_ActivationChannel = request.form.get("Census_ActivationChannel")
    Census_IsFlightsDisabled = request.form.get("Census_IsFlightsDisabled")
    Census_FlightRing = request.form.get("Census_FlightRing")
    Census_FirmwareManufacturerIdentifier = request.form.get("Census_FirmwareManufacturerIdentifier")
    Census_FirmwareVersionIdentifier = request.form.get("Census_FirmwareVersionIdentifier")
    Census_IsSecureBootEnabled = request.form.get("Census_IsSecureBootEnabled")
    Census_IsVirtualDevice = request.form.get("Census_IsVirtualDevice")
    Census_IsTouchEnabled = request.form.get("Census_IsTouchEnabled")
    Census_IsPenCapable = request.form.get("Census_IsPenCapable")
    Census_IsAlwaysOnAlwaysConnectedCapable = request.form.get("Census_IsAlwaysOnAlwaysConnectedCapable")
    Wdft_IsGamer = request.form.get("Wdft_IsGamer")
    Wdft_RegionIdentifier = request.form.get("Wdft_RegionIdentifier")
    Census_TotalPhysicalRAMGB = request.form.get("Census_TotalPhysicalRAMGB")
    Census_SystemVolumeTotalCapacityGB = request.form.get("Census_SystemVolumeTotalCapacityGB")
    Census_PrimaryDiskTotalCapacityGB = request.form.get("Census_PrimaryDiskTotalCapacityGB")

    # Cogemos los valores del de la petición POST (formato dicciones)
    f = request.form

    # Nos quedamos con las claves
    list_keys = []
    for key in f.keys():
        list_keys.append(key)
    print(list_keys)

    # Nos quedamos con los valores
    list_values = []
    for value in f.values():
        list_values.append(value)
    print(list_values)
    list_values = list(map(int, list_values))

    # Es necesario que el json esté en un formato adecuado
    # {"columns": ["alcohol", "chlorides", "citric_acid"], "data": [4, 4, 4]}
    print(json.dumps({"columns": list_keys, "data": [list_values]}))
    data = json.dumps({"columns": list_keys, "data": [list_values]})

    # Hacemos la petición, y nos quedamos con la salida (probabilidad)
    url = 'http://localhost:8002/invocations'
    headers = {"content-type": "application/json; format=pandas-split"}
    r = requests.post(url, data=data, headers=headers)

    return render_template("probabilidad_regresion_logistica.html", malware = r.text)


@app.route('/probabilidad_gradient_boosting',  methods=['POST'])
def probabilidad_gradient_boosting():

    '''
    Función que nos redirige a visualizar la probabilidad del algoritmo Gradient Boosting
    '''

    ProductName = request.form.get("ProductName")
    EngineVersion = request.form.get("EngineVersion")
    AppVersion = request.form.get("AppVersion")
    IsBeta = request.form.get("IsBeta")
    IsSxsPassiveMode = request.form.get("IsSxsPassiveMode")
    AVProductsInstalled = request.form.get("AVProductsInstalled")
    AVProductsEnabled = request.form.get("AVProductsEnabled")
    HasTpm = request.form.get("HasTpm")
    CountryIdentifier = request.form.get("CountryIdentifier")
    CityIdentifier = request.form.get("CityIdentifier")
    OrganizationIdentifier = request.form.get("OrganizationIdentifier")
    LocaleEnglishNameIdentifier = request.form.get("LocaleEnglishNameIdentifier")
    Platform = request.form.get("Platform")
    Processor = request.form.get("Processor")
    OsBuild = request.form.get("OsBuild")
    OsSuite = request.form.get("OsSuite")
    OsPlatformSubRelease = request.form.get("OsPlatformSubRelease")
    IsProtected = request.form.get("IsProtected")
    SMode = request.form.get("SMode")
    IeVerIdentifier = request.form.get("IeVerIdentifier")
    SmartScreen = request.form.get("SmartScreen")
    Firewall = request.form.get("Firewall")
    UacLuaenable = request.form.get("UacLuaenable")
    Census_MDC2FormFactor = request.form.get("Census_MDC2FormFactor")
    Census_DeviceFamily = request.form.get("Census_DeviceFamily")
    Census_OEMNameIdentifier = request.form.get("Census_OEMNameIdentifier")
    Census_OEMModelIdentifier = request.form.get("Census_OEMModelIdentifier")
    Census_ProcessorCoreCount = request.form.get("Census_ProcessorCoreCount")
    Census_ProcessorManufacturerIdentifier = request.form.get("")
    Census_PrimaryDiskTypeName = request.form.get("Census_PrimaryDiskTypeName")
    Census_HasOpticalDiskDrive = request.form.get("Census_HasOpticalDiskDrive")
    Census_ChassisTypeName = request.form.get("Census_ChassisTypeName")
    Census_InternalPrimaryDiagonalDisplaySizeInInches = request.form.get("Census_InternalPrimaryDiagonalDisplaySizeInInches")
    Census_InternalPrimaryDisplayResolutionHorizontal = request.form.get("Census_InternalPrimaryDisplayResolutionHorizontal")
    Census_PowerPlatformRoleName = request.form.get("Census_PowerPlatformRoleName")
    Census_InternalBatteryNumberOfCharges = request.form.get("Census_InternalBatteryNumberOfCharges")
    Census_OSBuildRevision = request.form.get("Census_OSBuildRevision")
    Census_OSEdition = request.form.get("Census_OSEdition")
    Census_OSInstallTypeName = request.form.get("Census_OSInstallTypeName")
    Census_OSInstallLanguageIdentifier = request.form.get("Census_OSInstallLanguageIdentifier")
    Census_OSWUAutoUpdateOptionsName = request.form.get("Census_OSWUAutoUpdateOptionsName")
    Census_IsPortableOperatingSystem = request.form.get("Census_IsPortableOperatingSystem")
    Census_GenuineStateName = request.form.get("Census_GenuineStateName")
    Census_ActivationChannel = request.form.get("Census_ActivationChannel")
    Census_IsFlightsDisabled = request.form.get("Census_IsFlightsDisabled")
    Census_FlightRing = request.form.get("Census_FlightRing")
    Census_FirmwareManufacturerIdentifier = request.form.get("Census_FirmwareManufacturerIdentifier")
    Census_FirmwareVersionIdentifier = request.form.get("Census_FirmwareVersionIdentifier")
    Census_IsSecureBootEnabled = request.form.get("Census_IsSecureBootEnabled")
    Census_IsVirtualDevice = request.form.get("Census_IsVirtualDevice")
    Census_IsTouchEnabled = request.form.get("Census_IsTouchEnabled")
    Census_IsPenCapable = request.form.get("Census_IsPenCapable")
    Census_IsAlwaysOnAlwaysConnectedCapable = request.form.get("Census_IsAlwaysOnAlwaysConnectedCapable")
    Wdft_IsGamer = request.form.get("Wdft_IsGamer")
    Wdft_RegionIdentifier = request.form.get("Wdft_RegionIdentifier")
    Census_TotalPhysicalRAMGB = request.form.get("Census_TotalPhysicalRAMGB")
    Census_SystemVolumeTotalCapacityGB = request.form.get("Census_SystemVolumeTotalCapacityGB")
    Census_PrimaryDiskTotalCapacityGB = request.form.get("Census_PrimaryDiskTotalCapacityGB")

    # Cogemos los valores del de la petición POST (formato dicciones)

    # Nos quedamos con las claves
    f = request.form
    list_keys = []
    for key in f.keys():
        list_keys.append(key)
    print(list_keys)

    # Nos quedamos con los valores
    list_values = []
    for value in f.values():
        list_values.append(value)
    print(list_values)

    # Es necesario que el json esté en un formato adecuado
    list_values = list(map(int, list_values))
    # {"columns": ["alcohol", "chlorides", "citric_acid"], "data": [4, 4, 4]}
    print(json.dumps({"columns": list_keys, "data": [list_values]}))
    data = json.dumps({"columns": list_keys, "data": [list_values]})

    # Hacemos la petición, y nos quedamos con la salida (probabilidad)
    url = 'http://localhost:8003/invocations'
    headers = {"content-type": "application/json; format=pandas-split"}
    r = requests.post(url, data=data, headers=headers)

    return render_template("probabilidad_gradient_boosting.html", malware = r.text)


if __name__ == "__main__":
    app.run(port=7000, debug=True)
