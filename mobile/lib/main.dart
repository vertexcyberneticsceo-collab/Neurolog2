import 'package:flutter/material.dart';

void main() {
  runApp(const NeurologApp());
}

class NeurologApp extends StatelessWidget {
  const NeurologApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Neurolog',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Neurolog'),
        ),
        body: const Center(
          child: Text('Neurolog Mobile App'),
        ),
      ),
    );
  }
}
