package com.elainehello.loginsystem.service;

import com.elainehello.loginsystem.entity.User;
import com.elainehello.loginsystem.repository.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

@Component
public class DataInitializer implements CommandLineRunner{

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    // Initialize properties/attributes
    public DataInitializer(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    public void run(String... args) {
        if (!userRepository.existsByEmail("test@example.com")) {
            User testUser = new User();
            testUser.setEmail("test@example.com");
            testUser.setPasswordHash(passwordEncoder.encode("password123"));
            testUser.setFirstName("Test");
            testUser.setLastName("User");
            testUser.setActive(true);

            userRepository.save(testUser);
            System.out.println("✅ Test user created: test@example.com / password123");
        }
    }
}
