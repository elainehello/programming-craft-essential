package com.elainehello.loginsystem.api.auth;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;

@Schema(description = "Response object containing authentication token")
public class LoginResponse {

    @JsonProperty("access_token")
    @Schema(description = "JWT access token for authentication", example = "abc123def456ghi789")
    private String accessToken;

    // (?) when to use 'final' properties/attributes
    @JsonProperty("expires_in")
    @Schema(description = "Token expiration time in seconds", example = "3600")
    private long expiresIn;

    public LoginResponse() {
     }

    // constructor initialize the attributes
    public LoginResponse(String accessToken, long expiresIn) {
        this.accessToken = accessToken;
        this.expiresIn = expiresIn;
    }
    
    // Getter and setter methods
    public String getAccessToken() {
        return accessToken;
    }

    public void setAccessToken(String accessToken) {
        this.accessToken = accessToken;
    }

    public long getExpiresIn() {
        return expiresIn;
    }

    public void setExpiresIn(long expiresIn) {
        this.expiresIn = expiresIn;
    }
}
