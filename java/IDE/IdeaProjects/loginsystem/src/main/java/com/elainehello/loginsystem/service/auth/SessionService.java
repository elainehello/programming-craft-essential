package com.elainehello.loginsystem.service.auth;

import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.time.Duration;
import java.util.UUID;

@Service
public class SessionService {

    private static final long TOKEN_EXPIRY_SECONDS = 3600L;
    private final RedisTemplate<String, String> redisTemplate;

    // Initialize property/attribute
    public SessionService(RedisTemplate<String, String> redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    /**
     * Create Mock fake token for a given userId
     * Later, replace with JWT or session management logic.
     */
    public String createAccessToken(String userId) {
        String token = userId + "-" + UUID.randomUUID().toString();
        // Store in Redis with expiration
        redisTemplate.opsForValue().set("token:" + token, userId, Duration.ofSeconds(TOKEN_EXPIRY_SECONDS));
        return token;
    }

    public boolean isValidToken(String token) {
        return redisTemplate.hasKey("token:" + token);
    }

    public void invalidateToken(String token) {
        redisTemplate.delete("token:" + token);
    }

    /**
     * Returns the token expiration time in seconds
     * Currently stubbed to 1 hour (3600 seconds)
     */
    public long getExpireIn() {
        return TOKEN_EXPIRY_SECONDS;
    }
}
