import 'dart:io';

import 'package:flutter/material.dart';
import 'dart:async';
import 'package:camera/camera.dart';
import 'package:glob/glob.dart';
import 'package:dio/dio.dart';
import 'package:http/http.dart' as http;

int cameraMode=0;

var files= Glob('/storage/emulated/0/DCIM/Camera/*.mp4');
class CameraScreen extends StatefulWidget {
  final List<CameraDescription> cameras;
  int cameraMode2;
  CameraScreen(this.cameras,this.cameraMode2);
  @override
  _CameraScreenState createState() => _CameraScreenState();
}

class _CameraScreenState extends State<CameraScreen> {
  CameraController controller;
  Dio dio= new Dio();
  Future<int> uploadImage(filename,url) async{
    var request= http.MultipartRequest('POST',Uri.parse(url));
    request.files.add(await http.MultipartFile.fromPath('video',filename));
    var res= await request.send();
    return res.statusCode;
  }
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    print("hello");
    print(files);
    controller= new CameraController(widget.cameras[cameraMode], ResolutionPreset.medium);
    controller.initialize().then((value) {
      if(!mounted){
        return;
      }
      setState(() {});
    });
  }
  @override
  void dispose() {
    // TODO: implement dispose
    controller?.dispose();
    super.dispose();
  }
  @override
  Widget build(BuildContext context) {
    if(!controller.value.isInitialized){
      return Container();
    }
    return Scaffold(
      backgroundColor: Colors.grey,
      appBar: AppBar(
        backgroundColor: Colors.teal,
        title: Center(
          child: Text(
            'Emotion Detector',
            textAlign: TextAlign.center,
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 35,
              color: Colors.white,
              fontFamily: 'Montserrat',
            ),
          ),
        ),
      ),
      body: Column(
        children: <Widget>[
          Container(
            margin: EdgeInsets.all(30),
            padding: EdgeInsets.all(30),
            child: AspectRatio(
                aspectRatio: controller.value.aspectRatio,
                child:CameraPreview(controller)
            ),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Material(
                elevation: 5.0,
                borderRadius: BorderRadius.circular(32.0),
                color: Colors.blue,
                child: MaterialButton(
                  minWidth: 10,
                  padding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
                  onPressed:() {
                    controller.startVideoRecording('/storage/emulated/0/DCIM/Camera/VideoTestRec.mp4');
                    print("started recording");
                  },
                  child: Text(
                    'Start Recording',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),
              Material(
                elevation: 5.0,
                borderRadius: BorderRadius.circular(32.0),
                color: Colors.blue,
                child: MaterialButton(
                  minWidth: 10,
                  padding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
                  onPressed:() {
                    controller.stopVideoRecording();
                    print("stopped recording");
                  },
                  child: Text(
                    'Stop Recording',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),
              Material(
                elevation: 5.0,
                borderRadius: BorderRadius.circular(32.0),
                color: Colors.blue,
                child: MaterialButton(
                  minWidth: 10,
                  padding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
                  onPressed:() {
                    print(cameraMode);
                    if(cameraMode==1)
                      cameraMode=0;
                    else
                      cameraMode=1;
                    controller=  CameraController(widget.cameras[cameraMode], ResolutionPreset.medium);
                      controller.initialize().then((value) {
                    if(!mounted){
                    return;
                      }
                      setState(() {});
                      });
                      },
                  child: Text(
                    'Rotate Camera',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),
            ],
          ),
          SizedBox(height: 25,),
          Material(
            elevation: 5.0,
            borderRadius: BorderRadius.circular(32.0),
            color: Colors.blue,
            child: MaterialButton(
              minWidth: 10,
              padding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
              onPressed:() async {
                FormData formData = new FormData.fromMap({
                  //'name':'videoUpload',
                'video': await MultipartFile.fromFile(
                '/storage/emulated/0/DCIM/Camera/VideoTestRec.mp4',
                //filename:"VideoTestRec.mp4"
                ),
                });
               var res= await dio.post('server_url',data: formData);
               print(res);


              },
              child: Text(
                'Upload to Server',
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}