import 'package:flutter/material.dart';

import 'api_service.dart';

void main() {
  runApp(const NeurologApp());
}

class NeurologApp extends StatelessWidget {
  const NeurologApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Neurolog',
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String status = 'Checking backend...';

  @override
  void initState() {
    super.initState();
    checkHealth();
  }

  Future<void> checkHealth() async {
    try {
      final result = await ApiService().health();

      setState(() {
        status = result['status'].toString();
      });
    } catch (_) {
      setState(() {
        status = 'Backend unavailable';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Neurolog'),
      ),
      body: Center(
        child: Text(status),
      ),
    );
  }
}
