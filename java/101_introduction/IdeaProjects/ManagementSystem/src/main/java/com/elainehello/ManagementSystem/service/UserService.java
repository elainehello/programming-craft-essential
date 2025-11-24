package com.elainehello.ManagementSystem.service;

import com.elainehello.ManagementSystem.model.entity.User;
import com.elainehello.ManagementSystem.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.Optional;
import java.util.*;

@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    // Create or Update User
    public User saveUser(User user) {
        return Optional.of(user)
                .map(userRepository::save)
                .orElseThrow(() -> new RuntimeException("User not saved"));
    }

    // Find user by ID
    public Optional<User> getUserById(Long id) {
        return Optional.ofNullable(id)
                .flatMap(userRepository::findById);
    }

    // Find user by Email
    public Optional<User> getUserByEmail(String email) {
        return Optional.ofNullable(email)
                .flatMap(userRepository::findByEmail);
    }

    // Get all Users
    public List<User> getAllUsers() {
        return Optional.of(userRepository.findAll())
                .orElseGet(Collections::emptyList);
    }

    // Get all User by first name
    public List<User> getUsersByFirstName(String firstName) {
        return Optional.ofNullable(firstName)
                .map(userRepository::findByFirstName)
                .orElse(List.of());
    }

    // Get all Users by last mame
    public List<User> getUsersByLastName(String lastName) {
        return Optional.of(lastName)
                .map(userRepository::findByLastName)
                .orElse(List.of());
    }

    // Find Users by first and/or last name
    public List<User> getUsersByFullName(String firstName, String lastName) {
        if (firstName != null && lastName != null) {
            return userRepository
                    .findByFirstNameAndLastName(firstName, lastName);
        } else if (firstName != null) {
            return userRepository.findByFirstName(firstName);
        }
        else if (lastName != null) {
            return userRepository.findByLastName(lastName);
        } else {
            return userRepository.findAll();
        }
    }

    // Delete user by ID
    public void deleteUserById(Long id) {
        Optional.ofNullable(id)
                .ifPresent(userRepository::deleteById);
    }

}
