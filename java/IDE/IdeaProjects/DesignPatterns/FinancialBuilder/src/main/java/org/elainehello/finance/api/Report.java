package org.elainehello.finance.api;


import java.util.ArrayList;
import java.util.List;

/*
*   The final complex product being built
*  */
public class Report {

    //atributes - properties
    private String format;
    private final List<String> sections = new ArrayList<>();

    public void setFormat(String format) {
        this.format = format;
    }

    public void addSection(String section) {
        sections.add(section);
    }

    public void display() {
        System.out.println("---Generating " + format + " Report---");
        sections.forEach(System.out::println);
        System.out.println("--------------------------------------");
    }
}
