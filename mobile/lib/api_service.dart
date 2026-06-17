import 'dart:convert';

import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://localhost:8000';

  Future<Map<String, dynamic>> health() async {
    final response = await http.get(
      Uri.parse('$baseUrl/health'),
    );

    return jsonDecode(response.body);
  }
}
