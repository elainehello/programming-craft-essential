package com.elainehello.loginsystem;

import org.springframework.boot.SpringApplication;

public class TestLoginsystemApplication {

	public static void main(String[] args) {
		SpringApplication.from(LoginsystemApplication::main).with(TestcontainersConfiguration.class).run(args);
	}

}
