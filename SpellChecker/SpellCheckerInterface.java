import java.util.*;

public interface SpellCheckerInterface
{
	public List<String> getIncorrectWords(String filename);
	public Set<String> getSuggestions(String word);
}
