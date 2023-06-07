package jhttp;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;

public class Meaning {
    private String id;
    private String text;
    private String exampleSentence;
    private String partOfSpeech;
    private List<String> antonyms;
    private List<String> synonyms;
    private String pronunciation;
    private int strength;

    // Constructors, getters, and setters

    @JsonProperty("id")
    public String getId() {
        return id;
    }

    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    @JsonProperty("text")
    public String getText() {
        return text;
    }

    @JsonProperty("text")
    public void setText(String text) {
        this.text = text;
    }

    @JsonProperty("partOfSpeech")
    public String getPartOfSpeech() {
        return partOfSpeech;
    }

    @JsonProperty("partOfSpeech")
    public void setPartOfSpeech(String partOfSpeech) {
        this.partOfSpeech = partOfSpeech;
    }

    @JsonProperty("exampleSentence")
    public String getExampleSentence() {
        return exampleSentence;
    }

    @JsonProperty("exampleSentence")
    public void setExampleSentence(String exampleSentence) {
        this.exampleSentence = exampleSentence;
    }

    @JsonProperty("antonyms")
    public List<String> getAntonyms() {
        return antonyms;
    }

    @JsonProperty("antonyms")
    public void setAntonyms(List<String> antonyms) {
        this.antonyms = antonyms;
    }

    @JsonProperty("synonyms")
    public List<String> getSynonyms() {
        return synonyms;
    }

    @JsonProperty("synonyms")
    public void setSynonyms(List<String> synonyms) {
        this.synonyms = synonyms;
    }

    @JsonProperty("pronunciation")
    public String getPronunciation() {
        return pronunciation;
    }

    @JsonProperty("pronunciation")
    public void setPronunciation(String pronunciation) {
        this.pronunciation = pronunciation;
    }

    @JsonProperty("strength")
    public int getStrength() {
        return strength;
    }

    @JsonProperty("strength")
    public void setStrength(int strength) {
        this.strength = strength;
    }
}
