package transporter.core.services.rule.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import transporter.core.services.rule.primitive.IRulePrimitive;
import transporter.core.services.rule.primitive.RecommendPrimitive;
import transporter.core.services.rule.primitive.WithdrawPrimitive;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;

import java.util.Map;

@Configuration
public class RuleService implements IRuleService {

    private static Logger logger = LoggerFactory.getLogger(RuleService.class);

    private final IRulePrimitive recommendService;
    private final IRulePrimitive withdrawService;

    @Autowired
    public RuleService(RecommendPrimitive recommendService, WithdrawPrimitive withdrawService) {
        this.recommendService = recommendService;
        this.withdrawService = withdrawService;
    }

    @Override
    public boolean classifier(Map<String, Object> obj) {
        // do classifying
        return false;
    }

    @Override
    public boolean classifier(String obj) {
        System.out.println(obj);
        recommendService.action(obj);
        withdrawService.action(obj);
        return false;
    }
}
