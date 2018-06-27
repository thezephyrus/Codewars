public class Kata {
  public static String chromosomeCheck(String sperm) {
    return (sperm.contains("XY") ? "Congratulations! You're going to have a son." : "Congratulations! You're going to have a daughter.");
  }
}

public class Kata {
    public static String chromosomeCheck(String sperm) {
        return "Congratulations! You're going to have a " + (sperm.contains("Y") ? "son." : "daughter.");
    }
}


public class Kata {
  public static String chromosomeCheck(String sperm) {
    return String.format("Congratulations! You're going to have a %s.", sperm == "XY" ? "son" : "daughter");
  }
}


public class Kata {
  public static String chromosomeCheck(String sperm) {
      if (sperm.contains("Y")) {
          return "Congratulations! You're going to have a son.";
      }
      return "Congratulations! You're going to have a daughter.";
  }
}


