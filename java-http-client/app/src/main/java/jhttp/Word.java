package jhttp;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.Map;

public class Word {
    private String id;
    private String spelling;
    private Map<String, Meaning> meanings;

    // Constructors, getters, and setters

    @JsonProperty("id")
    public String getId() {
        return id;
    }

    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    @JsonProperty("spelling")
    public String getSpelling() {
        return spelling;
    }

    @JsonProperty("spelling")
    public void setSpelling(String spelling) {
        this.spelling = spelling;
    }

    @JsonProperty("meanings")
    public Map<String, Meaning> getMeanings() {
        return meanings;
    }

    @JsonProperty("meanings")
    public void setMeanings(Map<String, Meaning> meanings) {
        this.meanings = meanings;
    }
}
