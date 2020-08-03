import 'dart:async';
import 'package:flutter/material.dart';
import 'cameraScreen.dart';
import 'LoginScreen.dart';
import 'package:camera/camera.dart';
//import 'package:simple_permissions/simple_permissions.dart';
var cameras;
//PermissionStatus permissionResult;
//Future<void> perm() async {
  //permissionResult = await SimplePermissions.requestPermission(
    //  Permission.WriteExternalStorage);
//}

Future<void> main() async{
  WidgetsFlutterBinding.ensureInitialized();
  cameras = await availableCameras();
  print(cameras);
  //perm();
    runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      routes: {
        '/': (context) => LoginScreen(cameras,1),
        '/cameraPage': (context) => CameraScreen(cameras,1),
      },
      initialRoute: '/',
    );
  }
}
