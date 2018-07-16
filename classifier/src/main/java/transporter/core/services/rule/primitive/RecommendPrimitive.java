package transporter.core.services.rule.primitive;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import transporter.core.model.rule.IRule;
import org.springframework.context.annotation.Configuration;

import java.util.List;
import java.util.Map;

@Configuration
public class RecommendPrimitive implements IRulePrimitive {

    private static Logger logger = LoggerFactory.getLogger(RecommendPrimitive.class);

    private List<IRule> recommendRules;

    @Override
    public boolean action(Map<String, Object> obj) {
        // do recommendation
        System.out.println("Do Recommendation");
        return false;
    }

    @Override
    public boolean action(String obj) {
        System.out.println("Recommend " + obj);
        return false;
    }
}
