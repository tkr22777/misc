/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package jhttp;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;

import static java.time.temporal.ChronoUnit.SECONDS;

public class App {
    public static void main(String[] args) throws JsonProcessingException {
        System.out.println("Hello!");
        //new App().testGetSuccess();
        //new App().testGetFailed();
        String wordString = new App().testGetWithPost();
        System.out.println("word string: " + wordString);
        Word word = toWord(wordString);
    }

    private static Word toWord(String wordString) throws JsonProcessingException {
        ObjectMapper objectMapper = new ObjectMapper();
        JsonNode node = objectMapper.readTree(wordString);
        System.out.println("word json node: " + node);
        return objectMapper.readValue(wordString, Word.class);
        //return null;
    }

    public void testGetSuccess() {
        try {
            URI uri = new URI("http://localhost:9000/api/v1");
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(uri)
                    .timeout(Duration.of(10, SECONDS))
                    .GET()
                    .build();

            HttpResponse<String> response = HttpClient.newBuilder()
                    .build()
                    .send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println("response status code: " + response.statusCode());
            System.out.println("response: " + response.body());
        } catch (Exception ex) {
        }
    }

    public void testGetFailed() {
        try {
            URI uri = new URI("http://localhost:9000/api/v2");
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(uri)
                    .timeout(Duration.of(10, SECONDS))
                    .GET()
                    .build();

            HttpResponse<String> response = HttpClient.newBuilder()
                    .build()
                    .send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println("response status code: " + response.statusCode());
            // System.out.println("response: " + response.body());
        } catch (Exception ex) {
        }
    }

    public String testGetWithPost() {
        HttpResponse<String> response = null;
        try {
            URI uri = new URI("http://localhost:9000/api/v1/words/postget");
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(uri)
                    .header("Content-Type", "application/json")
                    .timeout(Duration.of(10, SECONDS))
                    .POST(HttpRequest.BodyPublishers.ofString("{\"spelling\":\"ঙঢক\"}"))
                    .build();

            response = HttpClient.newBuilder()
                    .build()
                    .send(request, HttpResponse.BodyHandlers.ofString());

        } catch (Exception ex) {
        }
        return response.body();
    }
}